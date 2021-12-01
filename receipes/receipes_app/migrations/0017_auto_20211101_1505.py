# Generated by Django 3.2.8 on 2021-11-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0016_alter_receipe_diets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='category',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='grocery_aisle',
            field=models.CharField(choices=[('Baking', 'Baking'), ('Health Foods', 'Health Foods'), ('Spices and Seasonings', 'Spices and Seasonings'), ('Pasta and Rice', 'Pasta and Rice'), ('Bakery/Bread', 'Bakery/Bread'), ('Refrigerated', 'Refrigerated'), ('Canned and Jarred', 'Canned and Jarred'), ('Frozen', 'Frozen'), ('Nut butters, Jams, and Honey', 'Nut butters, Jams, and Honey'), ('Oil, Vinegar, Salad Dressing', 'Oil, Vinegar, Salad Dressing'), ('Condiments', 'Condiments'), ('Savory Snacks', 'Savory Snacks'), ('Milk, Eggs, Other Dairy', 'Milk, Eggs, Other Dairy'), ('Ethnic Foods', 'Ethnic Foods'), ('Tea and Coffee', 'Tea and Coffee'), ('Meat', 'Meat'), ('Gourmet', 'Gourmet'), ('Sweet Snacks', 'Sweet Snacks'), ('Gluten Free', 'Gluten Free'), ('Alcoholic Beverages', 'Alcoholic Beverages'), ('Cereal', 'Cereal'), ('Nuts', 'Nuts'), ('Beverages', 'Beverages'), ('Produce', 'Produce'), ('Not in Grocery Store/Homemade', 'Not in Grocery Store/Homemade'), ('Seafood', 'Seafood'), ('Cheese', 'Cheese'), ('Dried Fruits', 'Dried Fruits'), ('Online', 'Online'), ('Grilling Supplies', 'Grilling Supplies'), ('Bread', 'Bread')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='receipe',
            name='rating',
            field=models.FloatField(blank=True, default=None),
        ),
    ]