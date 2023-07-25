# Generated by Django 4.1.7 on 2023-07-14 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0005_user_first_name_user_last_name_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="online_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="authorUser",
                to="web.user",
            ),
        ),
    ]
