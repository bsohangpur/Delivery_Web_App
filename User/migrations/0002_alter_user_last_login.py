# Generated by Django 4.2.1 on 2023-05-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]