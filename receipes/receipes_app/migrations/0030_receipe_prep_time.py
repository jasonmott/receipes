# Generated by Django 3.2.9 on 2021-11-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0029_auto_20211109_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='prep_time',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
