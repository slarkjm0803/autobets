# Generated by Django 2.0.6 on 2019-11-21 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apimb', '0010_auto_20191115_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='runner',
            name='event',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apimb.Event'),
        ),
    ]