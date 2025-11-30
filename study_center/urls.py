"""
URL configuration for study_center project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# study_center/urls.py
from django.contrib import admin
from django.urls import path, include
from app.views import index, delete_student, portfolio, projects  # projects ni import qilishni unutmang!

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    
    # 1. Bosh sahifa (Portfolio)
    path('', portfolio, name='home'),
    
    # 2. CRM loyihasi (Endi /crm manzilida bo'ladi)
    path('crm/', index, name='crm_home'), # Ismini crm_home deb o'zgartirdik
    
    # 3. O'chirish funksiyasi
    path('delete/<int:id>/', delete_student, name='delete_student'),

    path('projects/', projects, name='projects'), # YANGI
]