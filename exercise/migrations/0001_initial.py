# Generated by Django 2.1 on 2018-08-24 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('exercise', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('units', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
