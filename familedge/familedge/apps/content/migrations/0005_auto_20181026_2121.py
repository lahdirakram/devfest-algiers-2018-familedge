# Generated by Django 2.1.2 on 2018-10-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20181026_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disipline',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]