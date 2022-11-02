from dataclasses import field
from django import forms
from .models import Employee 

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = Employee 
        fields = '__all__'
        widgets = {
            'Emp_ID' : forms.NumberInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'designation' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'experience' : forms.TextInput(attrs={'class':'form-control'}),
        }
