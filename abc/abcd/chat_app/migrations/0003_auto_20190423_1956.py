# Generated by Django 2.0.7 on 2019-04-23 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0002_auto_20190422_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='username',
            field=models.CharField(default='enter the valid username', max_length=50),
        ),
    ]
