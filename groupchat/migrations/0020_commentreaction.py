# Generated by Django 4.0.4 on 2022-05-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0019_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('user', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('comment', models.IntegerField()),
            ],
        ),
    ]