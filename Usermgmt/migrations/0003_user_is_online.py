# Generated by Django 4.2 on 2023-04-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Usermgmt", "0002_alter_user_email_alter_user_phone_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_online",
            field=models.BooleanField(default=False),
        ),
    ]
