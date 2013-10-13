# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        import os
        from django.core.management import call_command
        fixture = os.path.realpath(\
            os.path.join(\
                os.path.dirname(\
                    os.path.realpath(__file__)\
                    ), "initial_data.json"\
                )\
            )
        call_command("loaddata", fixture)
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."

    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True

