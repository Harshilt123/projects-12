from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, SubCategory, Transaction

# Category views
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

class CategoryCreateUpdateViewMixin:
    model = Category
    fields = ['name']
    template_name = 'category_form.html'

class CategoryCreateView(CategoryCreateUpdateViewMixin, CreateView):
    pass

class CategoryUpdateView(CategoryCreateUpdateViewMixin, UpdateView):
    pass

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    template_name = 'category_confirm_delete.html'

# Subcategory views
class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'subcategory_list.html'

class SubCategoryDetailView(DetailView):
    model = SubCategory
    template_name = 'subcategory_detail.html'

class SubCategoryCreateUpdateViewMixin:
    model = SubCategory
    fields = ['name', 'category']
    template_name = 'subcategory_form.html'

class SubCategoryCreateView(SubCategoryCreateUpdateViewMixin, CreateView):
    pass

class SubCategoryUpdateView(SubCategoryCreateUpdateViewMixin, UpdateView):
    pass

class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    success_url = reverse_lazy('subcategory_list')
    template_name = 'subcategory_confirm_delete.html'

# Transaction views
class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction_list.html'

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transaction_detail.html'

class TransactionCreateUpdateViewMixin:
    model = Transaction
    fields = ['amount', 'end_date', 'category', 'subcategory', 'payment', 'status']
    template_name = 'transaction_form.html'

class TransactionCreateView(TransactionCreateUpdateViewMixin, CreateView):
    pass

class TransactionUpdateView(TransactionCreateUpdateViewMixin, UpdateView):
    pass

class TransactionDeleteView(DeleteView):
    model = Transaction
    success_url = reverse_lazy('transaction_list')
    template_name = 'transaction_confirm_delete.html'
