# Generated by Django 5.0.4 on 2024-04-08 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_cad_exames", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="exame",
            name="usuario",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_cad_exames.usuario",
            ),
            preserve_default=False,
        ),
    ]
