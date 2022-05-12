# Generated by Django 4.0.4 on 2022-05-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0010_group_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.IntegerField()),
                ('message', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]