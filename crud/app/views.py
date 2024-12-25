from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
# Create your views here.

def index(request):
    data=Student.objects.all()
    context={'data':data}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def insertData(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=Student(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.info(request, "Data inserted successfully")
        return redirect('index')
    return render(request, 'index.html')

def updateData(request, id):
    d = Student.objects.get(id=id)
    
    if request.method == 'POST':
        d.name = request.POST.get('name')
        d.email = request.POST.get('email')
        d.age = request.POST.get('age')
        d.gender = request.POST.get('gender')
        d.save()
        messages.warning(request, "Data updated successfully")
        return redirect('index')
    
    context = {'d': d}
    return render(request, 'edit.html', context)

def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    messages.error(request, "Data deleted successfully")
    return redirect('index') 