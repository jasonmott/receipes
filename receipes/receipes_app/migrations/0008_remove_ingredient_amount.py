# Generated by Django 3.2.8 on 2021-10-31 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0007_auto_20211031_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='amount',
        ),
    ]
