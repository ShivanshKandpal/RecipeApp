from django import forms
from .models import Ingredient

# class IngredientForm(forms.Form):
#     ingredients = forms.ModelMultipleChoiceField(
#         queryset=Ingredient.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )
class IngredientForm(forms.Form):
    ingredient_names = forms.CharField(label='Ingredient Names', max_length=255)
