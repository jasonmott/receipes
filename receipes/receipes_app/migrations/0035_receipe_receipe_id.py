# Generated by Django 3.2.9 on 2021-11-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0034_auto_20211110_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
