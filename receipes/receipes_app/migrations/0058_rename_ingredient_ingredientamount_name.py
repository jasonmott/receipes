# Generated by Django 3.2.9 on 2021-11-14 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0057_receipe_ingredient_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientamount',
            old_name='ingredient',
            new_name='name',
        ),
    ]