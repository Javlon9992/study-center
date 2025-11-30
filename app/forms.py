# app/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['ism', 'familiya', 'telefon', 'fan', 'tolov_qildi'] # Yangilarini qo'shdik
        
        widgets = {
            'ism': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}),
            'familiya': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiya'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998...'}),
            'fan': forms.Select(attrs={'class': 'form-select'}), # Dropdown menyu
            'tolov_qildi': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'width: 20px; height: 20px;'}),
        }