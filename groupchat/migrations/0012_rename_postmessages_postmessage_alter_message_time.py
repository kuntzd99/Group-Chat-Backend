# Generated by Django 4.0.4 on 2022-05-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0011_post_postmessages_message_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostMessages',
            new_name='PostMessage',
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]