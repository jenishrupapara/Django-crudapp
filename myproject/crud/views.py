from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .form import StudentForm
from crud import form

# Create your views here.

def add(request):
    form = StudentForm(request.POST or None)
    #  Student = Student.objects.all()
    if form.is_valid():
        form.save()
    
    return render(request, 'add.html', {'form': form})
    
    
def show(request):
    student = Student.objects.all()
    student = Student.objects.all()
    return render(request, 'show.html', {'student': student})

def update(request, id):
    student = Student.objects.get(id=id) #   get_objects(id=id)  # This was your problem, Done!
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'student': student})

def delete(request, id):
    form = Student.objects.get(id=id) #   get_objects(id=id)
    form.delete()
    return HttpResponseRedirect('/')

