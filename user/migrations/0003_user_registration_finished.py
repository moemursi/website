# Generated by Django 2.2.10 on 2020-03-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("user", "0002_user_allow_empty_surname")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="registration_finished",
            field=models.BooleanField(default=False),
        )
    ]
