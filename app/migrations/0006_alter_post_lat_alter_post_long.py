# Generated by Django 4.2.16 on 2024-11-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_post_lat_post_long"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="lat",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="long",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
