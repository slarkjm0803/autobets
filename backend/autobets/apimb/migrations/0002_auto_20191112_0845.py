# Generated by Django 2.0.6 on 2019-11-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apimb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='runner',
            name='back_odds',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='runner',
            name='lay_odds',
            field=models.FloatField(null=True),
        ),
    ]