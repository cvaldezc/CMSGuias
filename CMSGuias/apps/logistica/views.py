# -*- coding: utf-8 -*-

import json

from django.db.models import Q, Count
from django.core import serializers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_list_or_404,get_object_or_404
from django.utils import simplejson
from django.utils.decorators import method_decorator
from django.template import RequestContext, TemplateDoesNotExist
from django.views.generic import TemplateView, View, ListView

from CMSGuias.apps.almacen.models import Suministro
from CMSGuias.apps.home.models import Proveedor, Documentos, FormaPago, Almacene, Moneda
from .models import Compra, Cotizacion, CotCliente, CotKeys, DetCotizacion, DetCompra, tmpcotizacion
from CMSGuias.apps.tools import genkeys, globalVariable


### Class Bases Views generic

# view home logistics
class LogisticsHome(TemplateView):
    template_name = "logistics/home.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LogisticsHome, self).dispatch(request, *args, **kwargs)

# Class view Supply
class SupplyPending(TemplateView):
    template_name = "logistics/supplypending.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = super(SupplyPending, self).get_context_data(**kwargs)
        if request.GET.get("rdo") is not None:
            if request.GET.get('rdo') == 'code':
                model = Suministro.objects.filter(pk=request.GET.get('id-su'),flag=True, status='PE')
            elif request.GET.get('rdo') == 'date':
                if request.GET.get('fi-su') != '' and request.GET.get('ff-su') == '':
                    messages.error(request, 'Ha ocurrido un error miestras se realizaba la consulta %s'%(str(request)))
                    model = Suministro.objects.filter(flag=True, status='PE', registrado__startswith=globalVariable.format_str_date(_str=request.GET.get('fi-su')))
                elif request.GET.get('fi-su') != '' and request.GET.get('ff-su') != '':
                    model = Suministro.objects.filter(flag=True, status='PE', registrado__range=(globalVariable.format_str_date(request.GET.get('fi-su')),globalVariable.format_str_date(request.GET.get('ff-su'))))
        else:
            model = Suministro.objects.filter(flag=True, status='PE')

        paginator = Paginator(model, 20)
        page = request.GET.get('page')
        try:
            supply = paginator.page(page)
        except PageNotAnInteger:
            supply = paginator.page(1)
        except EmptyPage:
            supply = paginator.page(paginator.num_pages)

        context['supply'] = supply
        context['status'] = globalVariable.status
        return render_to_response(self.template_name, context, context_instance=RequestContext(request))

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        context = {}
        if request.is_ajax():
            try:
                obj = Suministro.objects.get(flag=True, status='PE', pk=request.POST.get('id-su'))
                obj.status = 'AP' if request.POST.get('status') == "approve" else 'AN'
                obj.save() # update status supply
                context['status'] = True
            except ObjectDoesNotExist:
                messages.error(request, "Se ha encontrado error al cambiar el status de supply", messages.ERROR);
                raise Http404
                context['status'] = False
            context['type'] = request.POST.get('status')
            context = simplejson.dumps(context)
            return HttpResponse(context, mimetype="application/json", content_type="application/json")

# Class view Convert Supply to quote or Purchase
class SupplytoDocumentIn(TemplateView):
    template_name = "logistics/spdocumentin.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = super(SupplytoDocumentIn, self).get_context_data(**kwargs)
        model = Suministro.objects.filter(flag=True, status='AP')
        paginator = Paginator(model, 20)
        page = request.GET.get('page')
        try:
            supply = paginator.page(page)
        except PageNotAnInteger:
            supply = paginator.page(1)
        except EmptyPage:
            supply = paginator.page(paginator.num_pages)

        context['supply'] = supply
        context['status'] = globalVariable.status
        context['supplier'] = Proveedor.objects.filter(flag=True)
        context['storage'] = Almacene.objects.filter(flag=True)
        context['documents'] = Documentos.objects.filter(flag=True)
        context['payment'] = FormaPago.objects.filter(flag=True)
        context['currency'] = Moneda.objects.filter(flag=True)
        return render_to_response(self.template_name, context, context_instance=RequestContext(request))

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            if request.POST.get("type") == "finish":
                data = {}
                try:
                    obj =  Suministro.objects.get(pk=request.POST.get('supply'))
                    obj.status = 'CO'
                    obj.flag = False
                    obj.save()
                    data['obj'] = True
                except ObjectDoesNotExist, e:
                    data['status'] = False
                return HttpResponse(simplejson.dumps(data), mimetype='application/json', content_type='application/json')

            response = HttpResponse()
            data = {}
            try:
                # get status type document
                if request.POST.get('type') == "quote":
                    # saved quotation
                    idquote = None
                    if request.POST.get('newid') == "1":
                        # recover data for header quote and save
                        idquote = genkeys.GenerateKeyQuotation()
                        obj = Cotizacion()
                        obj.cotizacion_id = idquote
                        obj.suministro_id = request.POST.get('supply')
                        obj.empdni = request.user.get_profile().empdni
                        obj.almacen_id = request.POST.get('storage')
                        obj.traslado = globalVariable.format_str_date(request.POST.get('traslado'))
                        obj.obser = request.POST.get('obser')
                        obj.status = 'PE'
                        obj.flag = True
                        obj.save()
                    elif request.POST.get('newid') == "0":
                        idquote = request.POST.get('id')

                    # save quote to client
                    counter = CotKeys.objects.filter(cotizacion_id=idquote, proveedor_id=request.POST.get('supplier')).aggregate(counter=Count('cotizacion'))
                    if counter['counter'] == 0:
                        obj = CotKeys()
                        obj.cotizacion_id = idquote
                        obj.proveedor_id = request.POST.get('supplier')
                        obj.keygen = genkeys.GeneratekeysQuoteClient()
                        obj.status = "PE"
                        obj.flag = True
                        obj.save()

                    # save det quote
                    mats = json.loads(request.POST.get('mats'))
                    for x in range(mats.__len__()):
                        obj = DetCotizacion()
                        obj.cotizacion_id = idquote
                        obj.proveedor_id = request.POST.get('supplier')
                        obj.materiales_id = mats[x]['mid']
                        obj.cantidad = mats[x]['cant']
                        obj.flag = True
                        obj.save()

                    data["id"] = idquote
                    data['status'] = True
                elif request.POST.get('type') == "buy":
                    data['status'] = True
            except ObjectDoesNotExist, e:
                print e
                data['status'] = False
            response.write(simplejson.dumps(data))
            response['content_type'] = "application/json"
            response['mimetype'] = "application/json"
            return response

class ViewListQuotation(TemplateView):
    template_name = "logistics/listquotation.html"

    def get(self, request, *args, **kwargs):
        context = super(ViewListQuotation, self).get_context_data(**kwargs)
        if request.is_ajax():
            if request.GET.get('by') == 'code':
                model = CotKeys.objects.filter(cotizacion_id=request.GET.get('code'),flag=True)
            elif request.GET.get('by') == 'dates':
                if request.GET.get('dates') != '' and request.GET.get('datee') == '':
                    model = CotKeys.objects.filter(cotizacion__registrado__startswith=globalVariable.format_str_date(request.GET.get('dates')),flag=True)
                elif request.GET.get('dates') != '' and request.GET.get('datee') != '':
                    model = CotKeys.objects.filter(cotizacion__registrado__range=(globalVariable.format_str_date(request.GET.get('dates')),globalVariable.format_str_date(request.GET.get('datee'))), flag=True)
        else:
            model = CotKeys.objects.filter(flag=True)

        paginator = Paginator(model, 15)
        page = request.GET.get('page')
        try:
            quote = paginator.page(page)
        except PageNotAnInteger:
            quote = paginator.page(1)
        except EmptyPage:
            quote = paginator.page(paginator.num_pages)
        context['list'] = quote
        if request.is_ajax():
            data = {}
            data['list'] = [{'cotizacion_id':x.cotizacion_id,'proveedor_id':x.proveedor_id,'razonsocial':x.proveedor.razonsocial,'keygen':x.keygen,'traslado':globalVariable.format_date_str(x.cotizacion.traslado)} for x in quote]
            data['status'] = True
            return HttpResponse(simplejson.dumps(data), mimetype='application/json')
        else:
            return render_to_response(self.template_name, context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            context = dict()
            try:
                key = CotKeys.objects.get(cotizacion_id=request.POST.get('quote'),proveedor_id=request.POST.get('supplier'))
                if key.flag:
                    key.flag = False
                    key.save()
                flag = CotKeys.objects.filter(cotizacion_id=request.POST.get('quote'),proveedor_id=request.POST.get('supplier'), flag=True).aggregate(counter=Count('cotizacion'))
                if flag['counter'] == 0:
                    quote = Cotizacion.objects.get(cotizacion_id=request.POST.get('quote'))
                    quote.flag = False
                    quote.save()
                customer = CotCliente.objects.filter(cotizacion_id=request.POST.get('quote'),proveedor_id=request.POST.get('supplier'))
                if customer.__len__() > 0:
                    customer.flag = False
                    customer.save()
                context['status'] = True
            except ObjectDoesNotExist, e:
                raise e
                context['status'] = False
            return HttpResponse(simplejson.dumps(context), mimetype='application/json')

class ViewQuoteSingle(TemplateView):
    template_name = "logistics/single.html"

    def get(self, request, *args, **kwargs):
        context = super(ViewQuoteSingle, self).get_context_data(**kwargs)
        context['details'] = tmpcotizacion.objects.filter(empdni=request.user.get_profile().empdni).order_by('materiales__matnom')
        return render_to_response(self.template_name, context, context_instance=RequestContext(request))