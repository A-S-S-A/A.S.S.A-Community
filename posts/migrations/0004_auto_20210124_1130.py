# Generated by Django 3.1.5 on 2021-01-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_auto_20210124_1127"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="dislike",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="like",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
