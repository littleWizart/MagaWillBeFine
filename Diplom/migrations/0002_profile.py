# Generated by Django 5.0.6 on 2024-05-16 03:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diplom', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True)),
                ('klass', models.CharField(choices=[('5А', '5А'), ('5Б', '5Б'), ('5В', '5В'), ('5Г', '5Г'), ('6А', '6А'), ('6Б', '6Б'), ('6В', '6В'), ('6Г', '6Г'), ('7А', '7А'), ('7Б', '7Б'), ('7В', '7В'), ('7Г', '7Г'), ('8А', '8А'), ('8Б', '8Б'), ('8В', '8В'), ('8Г', '8Г'), ('9А', '9А'), ('9Б', '9Б'), ('9В', '9В'), ('9Г', '9Г'), ('10А', '10А'), ('10Б', '10Б'), ('10В', '10В'), ('10Г', '10Г'), ('11А', '11А'), ('11Б', '11Б'), ('11В', '11В'), ('11Г', '11Г')], max_length=4, verbose_name='Класс обучающегося')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
