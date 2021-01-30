# Generated by Django 3.1.5 on 2021-01-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_auto_20210124_0132"),
        ("users", "0011_auto_20210124_0040"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="like_posts",
            field=models.ManyToManyField(
                blank=True, related_name="like_users", to="posts.Post"
            ),
        ),
    ]
