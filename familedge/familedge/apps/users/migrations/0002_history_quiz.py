# Generated by Django 2.1.2 on 2018-10-26 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='quiz',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='content.quiz'),
            preserve_default=False,
        ),
    ]
