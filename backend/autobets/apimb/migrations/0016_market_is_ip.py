# Generated by Django 2.0.6 on 2019-11-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apimb', '0015_runner_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='is_ip',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
