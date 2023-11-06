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
    new_ingredients=forms.CharField(required=False)
    list_ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all().order_by('name'),label="list ingredients",widget=forms.CheckboxSelectMultiple)
    
    def getNewIngredients(self):
        return self.new_ingredients.split(',')
    class Meta:
        model = Dish
        # fields = ['name', 'directions', 'img_url', 'list_ingredient']
        exclude=['list_ingredient']
        