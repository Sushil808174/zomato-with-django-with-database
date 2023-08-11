from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'  # Include all fields from the model

class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=100)
    selected_items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.filter(availability=True),
        widget=forms.CheckboxSelectMultiple,
    )
    total_price = forms.DecimalField(initial=0, widget=forms.HiddenInput)
