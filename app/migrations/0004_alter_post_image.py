# Generated by Django 5.1.2 on 2024-11-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                default="app/static/images/urbex-icon.png", upload_to=""
            ),
        ),
    ]
