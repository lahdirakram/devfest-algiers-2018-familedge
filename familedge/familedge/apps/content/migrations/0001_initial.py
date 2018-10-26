# Generated by Django 2.1.2 on 2018-10-26 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='disipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='qst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('reponse', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('disipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.disipline')),
            ],
        ),
        migrations.CreateModel(
            name='user_disipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.disipline')),
            ],
        ),
        migrations.AddField(
            model_name='qst',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.quiz'),
        ),
        migrations.AddField(
            model_name='article',
            name='disipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.disipline'),
        ),
    ]
