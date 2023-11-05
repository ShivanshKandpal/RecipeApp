from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100,help_text='Enter the name of Ingredient')
    carbs = models.CharField(max_length=100,help_text = 'Enter carbohydrate content per 100 g')
    protein = models.CharField(max_length=100,help_text = 'Enter protein content per 100 g')
    fibre = models.CharField(max_length=100,help_text = 'Enter fibre content per 100 g')
    img_url = models.URLField(max_length=200)
    def __str__(self):
        return self.name
    
class Dish(models.Model):
    name = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    img_url = models.TextField()
    list_ingredient = models.ManyToManyField(Ingredient)
    def __str__(self):
        return self.name