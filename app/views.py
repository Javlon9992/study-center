# app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from .forms import StudentForm

# 1. Ro'yxatni ko'rish va Yangi qo'shish (bitta sahifada)
def index(request):
    students = Student.objects.all()# Bazadan hammasini olamiz
    # --- QIDIRUV MANTIG'I ---
    # 1. So'zni ushlab olamiz (masalan: "Ali")
    soz = request.GET.get('q', '') 
    
    # 2. Agar so'z bo'lsa, filtrlaymiz
    if soz:
        students = students.filter(
            Q(ism__icontains=soz) |       # Ismida bo'lsa... YOKI
            Q(familiya__icontains=soz) |  # Familiyasida bo'lsa... YOKI
            Q(telefon__icontains=soz)     # Telefonida bo'lsa...
        )
    # ------------------------

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()

    # Formadagi qidiruv so'zi o'chib ketmasligi uchun 'soz'ni ham qaytaramiz
    return render(request, 'index.html', {
        'students': students, 
        'form': form,
        'qidiruv_sozi': soz 
    })


    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() # Bazaga saqlash
            return redirect('index') # Sahifani yangilash
    else:
        form = StudentForm()

    return render(request, 'index.html', {'students': students, 'form': form})

# 2. O'chirish funksiyasi
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete() # Bazadan o'chirish
    return redirect('index')