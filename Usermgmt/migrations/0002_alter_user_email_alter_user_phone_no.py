# Generated by Django 4.2 on 2023-04-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Usermgmt", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, null=True, unique=True, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_no",
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
