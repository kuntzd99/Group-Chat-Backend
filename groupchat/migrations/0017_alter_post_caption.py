# Generated by Django 4.0.4 on 2022-05-13 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0016_invitation_group_invitation_sender_invitation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True),
        ),
    ]