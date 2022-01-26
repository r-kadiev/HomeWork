# Generated by Django 4.0.1 on 2022-01-23 23:25

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Statistic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("store", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=120)),
                ("status", models.CharField(blank=True, db_index=True, max_length=100)),
                ("day", models.DateField()),
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("unk", "Неизвестно"),
                            ("R_t", "Не хватило времени"),
                            ("R_f", "Форс-мажор"),
                            ("R_i", "Техническая проблема"),
                        ],
                        default="unk",
                        max_length=3,
                    ),
                ),
                ("timestamp", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
