"""
URL configuration for Attedance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


from django.contrib import admin
from django.urls import path, include
from app import views  # Replace 'your_app_name' with the actual app name



urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')), 
    # Ensure 'app' matches your actual Django app name
 
    path('', views.attendance_list, name='attendance_list'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path('mark_attendance/<int:attendance_id>/', views.mark_attendance, name='mark_attendance'),
    path('send_report/', views.send_report, name='send_report'),
    
    path('students/', views.students_list, name='students_list'),
]



