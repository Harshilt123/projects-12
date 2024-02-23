from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, help_text="User's age")
    salary = models.FloatField(null=True, blank=True, help_text="User's monthly salary")
    is_user = models.BooleanField(default=True, help_text="Flag indicating whether the user is active")

    class Meta:
        db_table = 'user'

    def clean(self):
        """
        Custom validation method to ensure age and salary have sensible values.
        """
        if self.age is not None and self.age <= 0:
            raise ValidationError("Age must be a positive integer.")

        if self.salary is not None and self.salary < 0:
            raise ValidationError("Salary must be a non-negative number.")
