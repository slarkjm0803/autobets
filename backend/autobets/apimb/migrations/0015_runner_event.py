# Generated by Django 2.0.6 on 2019-11-22 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apimb', '0014_runner_market'),
    ]

    operations = [
        migrations.AddField(
            model_name='runner',
            name='event',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apimb.Event'),
        ),
    ]
