# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # تأكد من أن لديك قالب HTML باسم home.html في مجلد القوالب
