from django import forms
from .models import Ingredient,Dish

# class IngredientForm(forms.Form):
#     ingredients = forms.ModelMultipleChoiceField(
#         queryset=Ingredient.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )
class IngredientForm(forms.Form):
    ingredient_names = forms.CharField(label='Ingredient Names', max_length=255,)
    
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'directions', 'img_url', 'list_ingredient']