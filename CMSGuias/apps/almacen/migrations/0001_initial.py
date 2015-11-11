# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pedido'
        db.create_table(u'almacen_pedido', (
            ('pedido_id', self.gf('django.db.models.fields.CharField')(default='PEAA000000', max_length=10, primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Proyecto'])),
            ('subproyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Subproyecto'], null=True, blank=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Sectore'], null=True, blank=True)),
            ('almacen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Almacene'])),
            ('asunto', self.gf('django.db.models.fields.CharField')(max_length=160, null=True)),
            ('empdni', self.gf('django.db.models.fields.related.ForeignKey')(default='70492850', to=orm['home.Employee'], null=True)),
            ('registrado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('traslado', self.gf('django.db.models.fields.DateField')()),
            ('obser', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='36', max_length=2)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('orderfile', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'almacen', ['Pedido'])

        # Adding model 'Detpedido'
        db.create_table(u'almacen_detpedido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pedido', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.Pedido'])),
            ('materiales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(default='BR000', to=orm['home.Brand'], blank=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(default='MO000', to=orm['home.Model'], blank=True)),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('cantshop', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('cantguide', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('spptag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['Detpedido'])

        # Adding model 'tmppedido'
        db.create_table(u'almacen_tmppedido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empdni', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('materiales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(default='BR000', to=orm['home.Brand'], blank=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(default='MO000', to=orm['home.Model'], blank=True)),
        ))
        db.send_create_signal(u'almacen', ['tmppedido'])

        # Adding model 'Niple'
        db.create_table(u'almacen_niple', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pedido', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.Pedido'])),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Proyecto'])),
            ('subproyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Subproyecto'], null=True, blank=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Sectore'], null=True, blank=True)),
            ('empdni', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('materiales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')(default=1, null=True)),
            ('metrado', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('cantshop', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('cantguide', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'almacen', ['Niple'])

        # Adding model 'tmpniple'
        db.create_table(u'almacen_tmpniple', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empdni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Employee'])),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Proyecto'], null=True, blank=True)),
            ('subproyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Subproyecto'], null=True, blank=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Sectore'], null=True, blank=True)),
            ('materiales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')(default=1, null=True)),
            ('metrado', self.gf('django.db.models.fields.FloatField')(default=1)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=250, null=True, blank=True)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['tmpniple'])

        # Adding model 'GuiaRemision'
        db.create_table(u'almacen_guiaremision', (
            ('guia_id', self.gf('django.db.models.fields.CharField')(max_length=12, primary_key=True)),
            ('pedido', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.Pedido'])),
            ('ruccliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Cliente'])),
            ('puntollegada', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('registrado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('traslado', self.gf('django.db.models.fields.DateField')()),
            ('traruc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Transportista'])),
            ('condni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Conductore'])),
            ('nropla', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Transporte'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='46', max_length=2)),
            ('motive', self.gf('django.db.models.fields.CharField')(default='VE', max_length=2, blank=True)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['GuiaRemision'])

        # Adding model 'DetGuiaRemision'
        db.create_table(u'almacen_detguiaremision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.GuiaRemision'])),
            ('materiales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('cantguide', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['DetGuiaRemision'])

        # Adding model 'NipleGuiaRemision'
        db.create_table(u'almacen_nipleguiaremision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.GuiaRemision'])),
            ('materiales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('metrado', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('cantguide', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['NipleGuiaRemision'])

        # Adding model 'Suministro'
        db.create_table(u'almacen_suministro', (
            ('suministro_id', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('almacen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Almacene'])),
            ('empdni', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('asunto', self.gf('django.db.models.fields.CharField')(max_length=180, null=True, blank=True)),
            ('registrado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('ingreso', self.gf('django.db.models.fields.DateField')()),
            ('obser', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='PE', max_length=2)),
            ('orders', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['Suministro'])

        # Adding model 'DetSuministro'
        db.create_table(u'almacen_detsuministro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('suministro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.Suministro'])),
            ('materiales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('cantshop', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(default='BR000', to=orm['home.Brand'], null=True, blank=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(default='MO000', to=orm['home.Model'], null=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('origin', self.gf('django.db.models.fields.CharField')(default='NN', max_length=10)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['DetSuministro'])

        # Adding model 'tmpsuministro'
        db.create_table(u'almacen_tmpsuministro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empdni', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('materiales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(default='BR000', to=orm['home.Brand'])),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(default='MO000', to=orm['home.Model'])),
            ('origin', self.gf('django.db.models.fields.CharField')(default='NN', max_length=2, null=True)),
            ('orders', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.Pedido'], null=True, blank=True)),
        ))
        db.send_create_signal(u'almacen', ['tmpsuministro'])

        # Adding model 'Inventario'
        db.create_table(u'almacen_inventario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('materiales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('almacen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Almacene'])),
            ('precompra', self.gf('django.db.models.fields.FloatField')()),
            ('preventa', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('stkmin', self.gf('django.db.models.fields.FloatField')()),
            ('stock', self.gf('django.db.models.fields.FloatField')()),
            ('stkpendiente', self.gf('django.db.models.fields.FloatField')()),
            ('stkdevuelto', self.gf('django.db.models.fields.FloatField')()),
            ('periodo', self.gf('django.db.models.fields.CharField')(default='', max_length=4)),
            ('ingreso', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('compra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistica.Compra'], null=True, blank=True)),
            ('spptag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['Inventario'])

        # Adding model 'InventoryBrand'
        db.create_table(u'almacen_inventorybrand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Almacene'])),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('materials', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Brand'])),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Model'])),
            ('ingress', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('stock', self.gf('django.db.models.fields.FloatField')()),
            ('purchase', self.gf('django.db.models.fields.FloatField')()),
            ('sale', self.gf('django.db.models.fields.FloatField')()),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['InventoryBrand'])

        # Adding model 'NoteIngress'
        db.create_table(u'almacen_noteingress', (
            ('ingress_id', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('storage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Almacene'])),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistica.Compra'])),
            ('guide', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('invoice', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('motive', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('register', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('receive', self.gf('django.db.models.fields.related.ForeignKey')(related_name='receiveAsEmployee', to=orm['home.Employee'])),
            ('inspection', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inspectionAsEmployee', to=orm['home.Employee'])),
            ('approval', self.gf('django.db.models.fields.related.ForeignKey')(related_name='approvalAsEmployee', to=orm['home.Employee'])),
            ('observation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='IN', max_length=2)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['NoteIngress'])

        # Adding model 'DetIngress'
        db.create_table(u'almacen_detingress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.NoteIngress'])),
            ('materials', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Materiale'])),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Brand'])),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Model'])),
            ('report', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['DetIngress'])

        # Adding model 'ReportInspect'
        db.create_table(u'almacen_reportinspect', (
            ('inspect', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('ingress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.NoteIngress'])),
            ('transport', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('arrival', self.gf('django.db.models.fields.DateField')()),
            ('instorage', self.gf('django.db.models.fields.DateField')()),
            ('register', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('boarding', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('observation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('empdni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Employee'])),
        ))
        db.send_create_signal(u'almacen', ['ReportInspect'])


    def backwards(self, orm):
        # Deleting model 'Pedido'
        db.delete_table(u'almacen_pedido')

        # Deleting model 'Detpedido'
        db.delete_table(u'almacen_detpedido')

        # Deleting model 'tmppedido'
        db.delete_table(u'almacen_tmppedido')

        # Deleting model 'Niple'
        db.delete_table(u'almacen_niple')

        # Deleting model 'tmpniple'
        db.delete_table(u'almacen_tmpniple')

        # Deleting model 'GuiaRemision'
        db.delete_table(u'almacen_guiaremision')

        # Deleting model 'DetGuiaRemision'
        db.delete_table(u'almacen_detguiaremision')

        # Deleting model 'NipleGuiaRemision'
        db.delete_table(u'almacen_nipleguiaremision')

        # Deleting model 'Suministro'
        db.delete_table(u'almacen_suministro')

        # Deleting model 'DetSuministro'
        db.delete_table(u'almacen_detsuministro')

        # Deleting model 'tmpsuministro'
        db.delete_table(u'almacen_tmpsuministro')

        # Deleting model 'Inventario'
        db.delete_table(u'almacen_inventario')

        # Deleting model 'InventoryBrand'
        db.delete_table(u'almacen_inventorybrand')

        # Deleting model 'NoteIngress'
        db.delete_table(u'almacen_noteingress')

        # Deleting model 'DetIngress'
        db.delete_table(u'almacen_detingress')

        # Deleting model 'ReportInspect'
        db.delete_table(u'almacen_reportinspect')


    models = {
        u'almacen.detguiaremision': {
            'Meta': {'ordering': "['materiales']", 'object_name': 'DetGuiaRemision'},
            'cantguide': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'guia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.GuiaRemision']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"})
        },
        u'almacen.detingress': {
            'Meta': {'object_name': 'DetIngress'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Brand']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.NoteIngress']"}),
            'materials': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Model']"}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'report': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'})
        },
        u'almacen.detpedido': {
            'Meta': {'ordering': "['materiales']", 'object_name': 'Detpedido'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'default': "'BR000'", 'to': u"orm['home.Brand']", 'blank': 'True'}),
            'cantguide': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'cantshop': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'default': "'MO000'", 'to': u"orm['home.Model']", 'blank': 'True'}),
            'pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.Pedido']"}),
            'spptag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tag': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'})
        },
        u'almacen.detsuministro': {
            'Meta': {'ordering': "['materiales']", 'object_name': 'DetSuministro'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'default': "'BR000'", 'to': u"orm['home.Brand']", 'null': 'True', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'cantshop': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'default': "'MO000'", 'to': u"orm['home.Model']", 'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'default': "'NN'", 'max_length': '10'}),
            'suministro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.Suministro']"}),
            'tag': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'})
        },
        u'almacen.guiaremision': {
            'Meta': {'object_name': 'GuiaRemision'},
            'condni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Conductore']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'guia_id': ('django.db.models.fields.CharField', [], {'max_length': '12', 'primary_key': 'True'}),
            'motive': ('django.db.models.fields.CharField', [], {'default': "'VE'", 'max_length': '2', 'blank': 'True'}),
            'nropla': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Transporte']"}),
            'pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.Pedido']"}),
            'puntollegada': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'registrado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'ruccliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Cliente']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'46'", 'max_length': '2'}),
            'traruc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Transportista']"}),
            'traslado': ('django.db.models.fields.DateField', [], {})
        },
        u'almacen.inventario': {
            'Meta': {'ordering': "['materiales']", 'object_name': 'Inventario'},
            'almacen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Almacene']"}),
            'compra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistica.Compra']", 'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingreso': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'materiales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'periodo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'precompra': ('django.db.models.fields.FloatField', [], {}),
            'preventa': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'spptag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stkdevuelto': ('django.db.models.fields.FloatField', [], {}),
            'stkmin': ('django.db.models.fields.FloatField', [], {}),
            'stkpendiente': ('django.db.models.fields.FloatField', [], {}),
            'stock': ('django.db.models.fields.FloatField', [], {})
        },
        u'almacen.inventorybrand': {
            'Meta': {'ordering': "['materials']", 'object_name': 'InventoryBrand'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Brand']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingress': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'materials': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Model']"}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'purchase': ('django.db.models.fields.FloatField', [], {}),
            'sale': ('django.db.models.fields.FloatField', [], {}),
            'stock': ('django.db.models.fields.FloatField', [], {}),
            'storage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Almacene']"})
        },
        u'almacen.niple': {
            'Meta': {'ordering': "['materiales']", 'object_name': 'Niple'},
            'cantguide': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.FloatField', [], {'default': '1', 'null': 'True'}),
            'cantshop': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'empdni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'metrado': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.Pedido']"}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Proyecto']"}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Sectore']", 'null': 'True', 'blank': 'True'}),
            'subproyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Subproyecto']", 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'almacen.nipleguiaremision': {
            'Meta': {'ordering': "['materiales']", 'object_name': 'NipleGuiaRemision'},
            'cantguide': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'guia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.GuiaRemision']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'metrado': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'almacen.noteingress': {
            'Meta': {'object_name': 'NoteIngress'},
            'approval': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'approvalAsEmployee'", 'to': u"orm['home.Employee']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'guide': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'ingress_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'inspection': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inspectionAsEmployee'", 'to': u"orm['home.Employee']"}),
            'invoice': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'motive': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistica.Compra']"}),
            'receive': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'receiveAsEmployee'", 'to': u"orm['home.Employee']"}),
            'register': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'IN'", 'max_length': '2'}),
            'storage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Almacene']"})
        },
        u'almacen.pedido': {
            'Meta': {'object_name': 'Pedido'},
            'almacen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Almacene']"}),
            'asunto': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True'}),
            'empdni': ('django.db.models.fields.related.ForeignKey', [], {'default': "'70492850'", 'to': u"orm['home.Employee']", 'null': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'obser': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'orderfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pedido_id': ('django.db.models.fields.CharField', [], {'default': "'PEAA000000'", 'max_length': '10', 'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Proyecto']"}),
            'registrado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Sectore']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'36'", 'max_length': '2'}),
            'subproyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Subproyecto']", 'null': 'True', 'blank': 'True'}),
            'traslado': ('django.db.models.fields.DateField', [], {})
        },
        u'almacen.reportinspect': {
            'Meta': {'object_name': 'ReportInspect'},
            'arrival': ('django.db.models.fields.DateField', [], {}),
            'boarding': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'empdni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Employee']"}),
            'ingress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.NoteIngress']"}),
            'inspect': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'instorage': ('django.db.models.fields.DateField', [], {}),
            'observation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'transport': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'almacen.suministro': {
            'Meta': {'ordering': "['suministro_id']", 'object_name': 'Suministro'},
            'almacen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Almacene']"}),
            'asunto': ('django.db.models.fields.CharField', [], {'max_length': '180', 'null': 'True', 'blank': 'True'}),
            'empdni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ingreso': ('django.db.models.fields.DateField', [], {}),
            'obser': ('django.db.models.fields.TextField', [], {}),
            'orders': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'registrado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PE'", 'max_length': '2'}),
            'suministro_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        },
        u'almacen.tmpniple': {
            'Meta': {'object_name': 'tmpniple'},
            'cantidad': ('django.db.models.fields.FloatField', [], {'default': '1', 'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'empdni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Employee']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'metrado': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Proyecto']", 'null': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Sectore']", 'null': 'True', 'blank': 'True'}),
            'subproyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Subproyecto']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'almacen.tmppedido': {
            'Meta': {'object_name': 'tmppedido'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'default': "'BR000'", 'to': u"orm['home.Brand']", 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'empdni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'default': "'MO000'", 'to': u"orm['home.Model']", 'blank': 'True'})
        },
        u'almacen.tmpsuministro': {
            'Meta': {'object_name': 'tmpsuministro'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'default': "'BR000'", 'to': u"orm['home.Brand']"}),
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'empdni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Materiale']"}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'default': "'MO000'", 'to': u"orm['home.Model']"}),
            'orders': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.Pedido']", 'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'default': "'NN'", 'max_length': '2', 'null': 'True'})
        },
        u'home.almacene': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Almacene'},
            'almacen_id': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'home.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'brand_id': ('django.db.models.fields.CharField', [], {'max_length': '5', 'primary_key': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'home.cargo': {
            'Meta': {'ordering': "['cargos']", 'object_name': 'Cargo'},
            'area': ('django.db.models.fields.CharField', [], {'default': "'Nothing'", 'max_length': '60'}),
            'cargo_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'primary_key': 'True'}),
            'cargos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'default': "'HH'", 'to': u"orm['home.Unidade']", 'null': 'True'})
        },
        u'home.cliente': {
            'Meta': {'ordering': "['razonsocial']", 'object_name': 'Cliente'},
            'contact': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Departamento']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'distrito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Distrito']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Pais']"}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Provincia']"}),
            'razonsocial': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ruccliente_id': ('django.db.models.fields.CharField', [], {'max_length': '11', 'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "'000-000-000'", 'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'home.conductore': {
            'Meta': {'object_name': 'Conductore'},
            'condni_id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'coninscription': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'conlic': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'connom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contel': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'traruc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Transportista']"})
        },
        u'home.departamento': {
            'Meta': {'ordering': "['depnom']", 'object_name': 'Departamento'},
            'departamento_id': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'depnom': ('django.db.models.fields.CharField', [], {'max_length': '56'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Pais']"})
        },
        u'home.distrito': {
            'Meta': {'ordering': "['distnom']", 'object_name': 'Distrito'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Departamento']"}),
            'distnom': ('django.db.models.fields.CharField', [], {'max_length': '56'}),
            'distrito_id': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Pais']"}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Provincia']"})
        },
        u'home.documentos': {
            'Meta': {'object_name': 'Documentos'},
            'documento': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'documento_id': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'home.employee': {
            'Meta': {'ordering': "['lastname']", 'object_name': 'Employee'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'birth': ('django.db.models.fields.DateField', [], {}),
            'charge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Cargo']"}),
            'empdni_id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'register': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'home.formapago': {
            'Meta': {'object_name': 'FormaPago'},
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pagos': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'pagos_id': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {})
        },
        u'home.materiale': {
            'Meta': {'ordering': "['matnom']", 'object_name': 'Materiale'},
            'matacb': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'matare': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'materiales_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15', 'primary_key': 'True'}),
            'matmed': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'matnom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Unidade']"})
        },
        u'home.model': {
            'Meta': {'object_name': 'Model'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Brand']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'model_id': ('django.db.models.fields.CharField', [], {'max_length': '5', 'primary_key': 'True'})
        },
        u'home.moneda': {
            'Meta': {'object_name': 'Moneda'},
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'moneda': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'moneda_id': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'simbolo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5'})
        },
        u'home.pais': {
            'Meta': {'ordering': "['paisnom']", 'object_name': 'Pais'},
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pais_id': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'}),
            'paisnom': ('django.db.models.fields.CharField', [], {'max_length': '56'})
        },
        u'home.proveedor': {
            'Meta': {'ordering': "['razonsocial']", 'object_name': 'Proveedor'},
            'contact': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Departamento']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'distrito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Distrito']"}),
            'email': ('django.db.models.fields.CharField', [], {'default': "'ejemplo@dominio.com'", 'max_length': '60'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'origen': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Pais']"}),
            'proveedor_id': ('django.db.models.fields.CharField', [], {'max_length': '11', 'primary_key': 'True'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Provincia']"}),
            'razonsocial': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        u'home.provincia': {
            'Meta': {'ordering': "['pronom']", 'object_name': 'Provincia'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Departamento']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Pais']"}),
            'pronom': ('django.db.models.fields.CharField', [], {'max_length': '56'}),
            'provincia_id': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'})
        },
        u'home.transporte': {
            'Meta': {'object_name': 'Transporte'},
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nropla_id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'traruc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Transportista']"})
        },
        u'home.transportista': {
            'Meta': {'object_name': 'Transportista'},
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tranom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'traruc_id': ('django.db.models.fields.CharField', [], {'max_length': '11', 'primary_key': 'True'}),
            'tratel': ('django.db.models.fields.CharField', [], {'default': "'000-000-000'", 'max_length': '11', 'null': 'True'})
        },
        u'home.unidade': {
            'Meta': {'object_name': 'Unidade'},
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'unidad_id': ('django.db.models.fields.CharField', [], {'max_length': '7', 'primary_key': 'True'}),
            'uninom': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'logistica.compra': {
            'Meta': {'ordering': "['compra_id']", 'object_name': 'Compra'},
            'compra_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cotizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistica.Cotizacion']", 'null': 'True', 'blank': 'True'}),
            'deposito': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'documento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Documentos']", 'null': 'True', 'blank': 'True'}),
            'empdni': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['home.Employee']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lugent': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Moneda']", 'null': 'True', 'blank': 'True'}),
            'pagos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.FormaPago']", 'null': 'True', 'blank': 'True'}),
            'projects': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Proveedor']"}),
            'registrado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PE'", 'max_length': '2'}),
            'traslado': ('django.db.models.fields.DateField', [], {})
        },
        u'logistica.cotizacion': {
            'Meta': {'ordering': "['cotizacion_id']", 'object_name': 'Cotizacion'},
            'almacen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Almacene']"}),
            'cotizacion_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'empdni': ('django.db.models.fields.related.ForeignKey', [], {'default': "'70492850'", 'to': u"orm['home.Employee']"}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'obser': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'registrado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PE'", 'max_length': '2'}),
            'suministro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.Suministro']", 'null': 'True', 'blank': 'True'}),
            'traslado': ('django.db.models.fields.DateField', [], {})
        },
        u'ventas.proyecto': {
            'Meta': {'ordering': "['nompro']", 'object_name': 'Proyecto'},
            'approved': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'approvedAsEmployee'", 'null': 'True', 'to': u"orm['home.Employee']"}),
            'comienzo': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Moneda']", 'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Departamento']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'distrito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Distrito']"}),
            'empdni': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'proyectoAsEmployee'", 'null': 'True', 'to': u"orm['home.Employee']"}),
            'exchange': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'nompro': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'obser': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Pais']"}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Provincia']"}),
            'proyecto_id': ('django.db.models.fields.CharField', [], {'max_length': '7', 'primary_key': 'True'}),
            'registrado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'ruccliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Cliente']", 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'00'", 'max_length': '2'}),
            'typep': ('django.db.models.fields.CharField', [], {'default': "'ACI'", 'max_length': '3'})
        },
        u'ventas.sectore': {
            'Meta': {'ordering': "['sector_id']", 'object_name': 'Sectore'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'amountsales': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'atype': ('django.db.models.fields.CharField', [], {'default': "'NN'", 'max_length': '2', 'blank': 'True'}),
            'comienzo': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'nomsec': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'obser': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'planoid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16', 'null': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Proyecto']"}),
            'registrado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sector_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'AC'", 'max_length': '2'}),
            'subproyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Subproyecto']", 'null': 'True', 'blank': 'True'})
        },
        u'ventas.subproyecto': {
            'Meta': {'ordering': "['nomsub']", 'object_name': 'Subproyecto'},
            'additional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comienzo': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'nomsub': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'obser': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Proyecto']"}),
            'registrado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'AC'", 'max_length': '2'}),
            'subproyecto_id': ('django.db.models.fields.CharField', [], {'max_length': '7', 'primary_key': 'True'})
        }
    }

    complete_apps = ['almacen']