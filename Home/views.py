from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm
from django.contrib.auth.models import User, auth
# Create your views here.


def login(request):
    return render(request, 'login.html')
    # if request.method == 'post':
    #     username = request.post['username']
    #     password = request.post['password']
    #
    #     user = auth.authenticate(username=username, password=password)
    #     if user is not None:
    #         print('hello none')
    #         auth.login(request, user)
    #         return render('department.html')
    #     else:
    #         return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)


def contact(request):
    return render(request, 'contact.html')


def doctors(request):
    dict_doc = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_doc)


def department(request):
    dict_dpt = {
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dpt)
