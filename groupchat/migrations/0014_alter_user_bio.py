# Generated by Django 4.0.4 on 2022-05-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0013_group_image_user_bio_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]