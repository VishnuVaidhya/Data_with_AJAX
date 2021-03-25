from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from . forms import StudentForm, Student
# Create your views here.

def Home(request):
    return render(request, 'student/base.html')

def Register(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    else:
        fm = UserCreationForm()
    template_name = 'student/register.html'
    context = {'form': fm}
    return render(request, template_name, context)


def Login_View(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('student_add')

    else:
        fm = AuthenticationForm()
    template_name = 'student/login.html'
    context = {'form': fm}
    return render(request, template_name, context)

def Logout_view(request):
    logout(request)
    return redirect('login')

def Student_Add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
        template_name = 'Student/add_student.html'
        context = {'form': form}
        return render(request, template_name, context)

def Student_alldata(request):
    studs = list(Student.objects.all().values())
    data = {'studs': studs}
    return JsonResponse(data)