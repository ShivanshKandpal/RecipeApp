# Generated by Django 4.2.6 on 2023-11-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ingredient', '0004_remove_ingredient_carbs_remove_ingredient_fibre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='carbs',
            field=models.CharField(default=1, help_text='Enter carbohydrate content per serve', max_length=100),
        ),
        migrations.AlterField(
            model_name='dish',
            name='fat',
            field=models.CharField(default=1, help_text='Enter fat content per serve', max_length=100),
        ),
        migrations.AlterField(
            model_name='dish',
            name='protein',
            field=models.CharField(default=1, help_text='Enter protein content per serve', max_length=100),
        ),
    ]