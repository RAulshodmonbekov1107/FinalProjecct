# forms.py

from django import forms
from .models import PerformanceEvaluation

class PerformanceEvaluationForm(forms.ModelForm):
    class Meta:
        model = PerformanceEvaluation
        fields = ['employee', 'evaluation_date', 'performance_rating', 'comments']
        widgets = {
            'evaluation_date': forms.DateInput(attrs={'type': 'date'}),
            'performance_rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'comments': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'employee': 'Employee',
            'evaluation_date': 'Evaluation Date',
            'performance_rating': 'Performance Rating (1-10)',
            'comments': 'Comments',
        }
# forms.py

from .models import Payroll

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'pay_period_start_date', 'pay_period_end_date', 'hours_worked', 'overtime_hours', 'gross_pay', 'deductions', 'net_pay']
        widgets = {
            'pay_period_start_date': forms.DateInput(attrs={'type': 'date'}),
            'pay_period_end_date': forms.DateInput(attrs={'type': 'date'}),
        }
