# Generated by Django 3.1.5 on 2021-02-01 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210201_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
