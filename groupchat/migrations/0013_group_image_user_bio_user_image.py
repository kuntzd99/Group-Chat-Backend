# Generated by Django 4.0.4 on 2022-05-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0012_rename_postmessages_postmessage_alter_message_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]