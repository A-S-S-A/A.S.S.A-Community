# Generated by Django 3.1.5 on 2021-01-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_user_superhost"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="homepage",
            field=models.URLField(blank=True, null=True),
        ),
    ]
