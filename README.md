# 🎓 Study Center CRM

O'quv markazlari uchun talabalarni boshqarish tizimi (CRM).
Ushbu tizim orqali administratorlar talabalarni ro'yxatga olishi, to'lovlarni nazorat qilishi va kurslar bo'yicha filtrlashi mumkin.

🌐 **Jonli Demo:** [https://jetjava.uz](https://jetjava.uz)

## 🛠 Texnologiyalar
* **Backend:** Python, Django 5
* **Frontend:** HTML5, Bootstrap 5
* **Database:** SQLite (Productionda PostgreSQL ga o'tish rejalashtirilgan)
* **Deployment:** Ubuntu VPS, Nginx, Gunicorn, SSL (Let's Encrypt)

## 🚀 Imkoniyatlar
- [x] Talabalar CRUD (Qo'shish, O'qish, O'chirish)
- [x] Qidiruv tizimi va Filtrlash
- [x] To'lov holatini monitoring qilish (Yashil/Qizil status)
- [x] Admin panel orqali boshqaruv
- [x] To'liq moslashuvchan (Mobile Responsive) dizayn

## 📦 O'rnatish
```bash
git clone [https://github.com/SizningNikingiz/study-center.git](https://github.com/SizningNikingiz/study-center.git)
cd study-center
pip install -r requirements.txt
python manage.py runserver
