from django.db import models
from django.core.validators import MinValueValidator
PAYMENT_CHOICES = [
    ('credit', 'Credit'),
    ('cash', 'Cash'),
    ('cheque', 'Cheque'),
]
STATUS_CHOICES = [
    ('cleared', 'Cleared'),
    ('uncleared', 'Uncleared'),
    ('void', 'Void'),
]

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Subcategory Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subcategories"

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    end_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Subcategory")
    payment = models.CharField(max_length=50, choices=PAYMENT_CHOICES, verbose_name="Payment Method")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="Status")

    def __str__(self):
        return f"Transaction ID: {self.id}"
