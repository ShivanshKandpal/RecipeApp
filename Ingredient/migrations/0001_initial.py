# Generated by Django 4.2.6 on 2023-11-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of Ingredient', max_length=100)),
                ('carbs', models.CharField(help_text='Enter carbohydrate content per 100 g', max_length=100)),
                ('protein', models.CharField(help_text='Enter protein content per 100 g', max_length=100)),
                ('fibre', models.CharField(help_text='Enter fibre content per 100 g', max_length=100)),
                ('img_url', models.URLField()),
            ],
        ),
    ]