from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'forms/add_student.html', {'form': form})

def students_list(request):
    students = Student.objects.all()
    return render(request, 'forms/students_list.html', {'students': students})
