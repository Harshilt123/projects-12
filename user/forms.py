from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class UserRegistrationForm(UserCreationForm):
    age = forms.IntegerField(min_value=0)
    salary = forms.FloatField(min_value=0)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'age', 'salary', 'password1', 'password2']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_user = True
        if commit:
            user.save()
        return user

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age <= 0:
            raise forms.ValidationError('Age must be a positive integer.')
        return age

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is not None and salary < 0:
            raise forms.ValidationError('Salary must be a non-negative number.')
        return salary
