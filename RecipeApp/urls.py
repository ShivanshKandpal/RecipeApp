"""
URL configuration for RecipeApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Ingredient.views import indexView,createview,recipe_search,recipe_detail,create_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexView),
    # path('SearchRecipe/',searchview),
    path('CreateRecipe',createview),
    path('recipe_search/',recipe_search,name='recipe_search'),
    path('recipe_detail/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('create_recipe/',create_recipe, name='create_recipe'),
]
