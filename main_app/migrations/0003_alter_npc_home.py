# Generated by Django 4.0.4 on 2022-05-08 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_npc_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npc',
            name='home',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.location'),
        ),
    ]
