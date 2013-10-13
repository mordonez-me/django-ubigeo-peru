# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ubigeo'
        db.create_table(u'ubigeo_ubigeo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('political_division', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('lat', self.gf('django.db.models.fields.TextField')()),
            ('lon', self.gf('django.db.models.fields.TextField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubigeo.Ubigeo'], null=True)),
        ))
        db.send_create_signal(u'ubigeo', ['Ubigeo'])


    def backwards(self, orm):
        # Deleting model 'Ubigeo'
        db.delete_table(u'ubigeo_ubigeo')


    models = {
        u'ubigeo.ubigeo': {
            'Meta': {'object_name': 'Ubigeo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.TextField', [], {}),
            'lon': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubigeo.Ubigeo']", 'null': 'True'}),
            'political_division': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['ubigeo']