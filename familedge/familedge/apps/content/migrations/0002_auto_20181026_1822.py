# Generated by Django 2.1.2 on 2018-10-26 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_disipline',
            name='disipline',
        ),
        migrations.DeleteModel(
            name='user_disipline',
        ),
    ]
