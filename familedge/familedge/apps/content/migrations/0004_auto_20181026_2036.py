# Generated by Django 2.1.2 on 2018-10-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='disipline',
            name='image',
            field=models.FileField(default='images/1.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='disipline',
            name='quote',
            field=models.TextField(default='this is suposed to be a quote'),
        ),
    ]