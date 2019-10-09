# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-03 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0037_jobapplication_challenge_resent")]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="salary_range",
            field=models.IntegerField(
                choices=[
                    (1, "R$ 0,00 a R$ 1.000,00"),
                    (2, "R$ 1.000,01 a R$ 3.000,00"),
                    (3, "R$ 3.000,01 a R$ 6.000,00"),
                    (4, "R$ 6.000,01 a R$ 10.000,00"),
                    (5, "R$ 10.000,01 ou R$ 13.000,00"),
                    (6, "R$ 13.000,01 ou R$ 16.000,00"),
                    (6, "R$ 16.000,01 ou R$ 19.000,00"),
                    (6, "R$ 19.000,01 ou R$ 21.000,00"),
                    (6, "R$ 21.000,01 ou mais"),
                    (7, "A combinar"),
                ],
                default=6,
                verbose_name="Faixa Salarial",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="salary_range",
            field=models.IntegerField(
                choices=[
                    (1, "R$ 0,00 a R$ 1.000,00"),
                    (2, "R$ 1.000,01 a R$ 3.000,00"),
                    (3, "R$ 3.000,01 a R$ 6.000,00"),
                    (4, "R$ 6.000,01 a R$ 10.000,00"),
                    (5, "R$ 10.000,01 ou R$ 13.000,00"),
                    (6, "R$ 13.000,01 ou R$ 16.000,00"),
                    (6, "R$ 16.000,01 ou R$ 19.000,00"),
                    (6, "R$ 19.000,01 ou R$ 21.000,00"),
                    (6, "R$ 21.000,01 ou mais"),
                    (7, "A combinar"),
                ],
                default=6,
                verbose_name="Sua Faixa Salarial Atual",
            ),
        ),
    ]
