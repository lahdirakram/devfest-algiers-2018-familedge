# Generated by Django 2.1.2 on 2018-10-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
