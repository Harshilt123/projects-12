from django import forms
from .models import Category, SubCategory, Transaction

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'end_date', 'category', 'subcategory', 'payment', 'status']
