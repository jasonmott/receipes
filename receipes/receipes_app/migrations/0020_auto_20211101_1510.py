# Generated by Django 3.2.8 on 2021-11-01 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0019_auto_20211101_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientamount',
            old_name='possibleUnits',
            new_name='select_Type_of_Unit',
        ),
        migrations.RemoveField(
            model_name='ingredientamount',
            name='unit',
        ),
    ]
