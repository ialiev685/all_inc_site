# Generated by Django 5.1.3 on 2024-11-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CountryModel",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=50)),
                ("alias", models.CharField(blank=True, max_length=50)),
                ("flags", models.IntegerField(blank=True)),
                ("has_tickets", models.BooleanField(blank=True)),
                ("hotel_is_not_in_stop", models.BooleanField(blank=True)),
                ("is_visa", models.BooleanField(blank=True)),
                ("is_pro_visa", models.BooleanField(blank=True)),
                ("original_name", models.CharField(blank=True, max_length=100)),
                ("rank", models.IntegerField(blank=True)),
                ("tickets_included", models.BooleanField(blank=True)),
            ],
        ),
    ]