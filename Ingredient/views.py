from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

def indexView(request):
    # all_ingredients = ingredientItem.objects.all()
    return render(request, 'index.html')

def sbrview(request):
    return render(request,'sbr.html')

