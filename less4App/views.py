from django.shortcuts import render, redirect
from .models import Employee
from less4App.forms import EmployeeForm

from django.core.paginator import Paginator
from django.contrib import messages

from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.conf import settings

from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from less4App.forms import ContactForm

# Create your views here.
def index(request):
    emp = Employee.objects.all()

    context = {'title': 'Welcome', 'employees': emp}
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.error(request,'Insert successfully ')
                return redirect('/')
            except Exception as e:
                print("type error: " + str(e))
        else:
            pass
    else:
        form = EmployeeForm()
    return render(request,'create.html',{'form':form})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,request.FILES) #try
    return render(request,'edit.html',{'employee':employee,'form':form})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,request.FILES,instance=employee)
    if form.is_valid():
        try:
            form.save()
            messages.error(request,'Update successfully ')
            return redirect('/')
        except Exception as e:
                print("type error: " + str(e))
    else:
        messages.error(request,form.errors)

    return render(request, 'edit.html', {'employee': employee,'form':form})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['to']
            message = form.cleaned_data['message']

            recipient_list = []
            recipient_list.append(from_email)
            try:
                emailobj = EmailMessage(subject, message, to=recipient_list)
                emailobj.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/')
    return render(request, "email.html", {'form': form})

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['to']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['nazmul@daffodil.ac'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message. 2')
