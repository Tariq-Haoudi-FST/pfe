from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # قم بتعريف المسار وعرض الصفحة الرئيسية
]
