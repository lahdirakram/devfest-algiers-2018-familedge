# Generated by Django 2.1.2 on 2018-10-27 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_fami'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='objective',
            new_name='goals',
        ),
    ]