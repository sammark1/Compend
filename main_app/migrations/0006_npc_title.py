# Generated by Django 4.0.4 on 2022-05-12 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_location_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='npc',
            name='title',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
