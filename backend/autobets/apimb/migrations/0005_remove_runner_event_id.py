# Generated by Django 2.0.6 on 2019-11-12 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimb', '0004_auto_20191112_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runner',
            name='event_id',
        ),
    ]
