# Generated by Django 5.0.2 on 2024-02-22 09:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Subcategory Name'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment',
            field=models.CharField(choices=[('credit', 'Credit'), ('cash', 'Cash'), ('cheque', 'Cheque')], max_length=50, verbose_name='Payment Method'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('cleared', 'Cleared'), ('uncleared', 'Uncleared'), ('void', 'Void')], max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp.subcategory', verbose_name='Subcategory'),
        ),
    ]
