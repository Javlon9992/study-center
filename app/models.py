# app/models.py
from django.db import models

class Student(models.Model):
    # Kurslar ro'yxati (Tanlash uchun)
    KURSLAR = [
        ('Python', 'Python Backend'),
        ('Frontend', 'Frontend (React)'),
        ('English', 'English Language'),
        ('SMM', 'SMM & Marketing'),
    ]

    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    telefon = models.CharField(max_length=20)
    
    # YANGI QO'SHILGANLAR:
    fan = models.CharField(max_length=20, choices=KURSLAR, default='Python')
    tolov_qildi = models.BooleanField(default=False) # True=To'lagan, False=Qarzdor

    def __str__(self):
        return self.ism