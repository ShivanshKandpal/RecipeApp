from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import IngredientForm
import json
from .models import Dish
from django.views.decorators.csrf import csrf_exempt

def indexView(request):
    # all_ingredients = ingredientItem.objects.all()
    return render(request, 'index.html')

# def searchview(request):
#     return render(request,'search.html')

def createview(request):
    return render(request,'create.html')

def recipe_search(request):
    recipes = Dish.objects.all()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            selected_ingredients = form.cleaned_data['ingredient_names'].split()
            # recipes =  Dish.objects.filter(list_ingredient__in = selected_ingredients).distinct()
            for ing in selected_ingredients:
                recipes = recipes.filter(list_ingredient__name__icontains=ing).distinct()
        else:
            recipes = []
    else:
        form = IngredientForm()
        recipes = []
    context = {
        'form': form,
        'recipes': recipes,
    }
    return render(request, 'recipe_search.html', context)
        
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Dish, pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})