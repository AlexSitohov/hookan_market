# Generated by Django 4.1 on 2022-09-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='suma_all',
        ),
    ]
