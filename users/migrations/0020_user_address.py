# Generated by Django 3.1.5 on 2021-02-09 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
