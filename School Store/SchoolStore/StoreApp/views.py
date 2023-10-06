from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Courses,Department
from .forms import StoreForm
# Create your views here.
def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid User")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('register')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def store_form(request):


    if request.method == 'POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        course=request.POST.get('course')
        form=StoreForm({'department':department,'course':course,'name':name})
        if form.is_valid():
            form.save()
            return redirect('msg')
        else:
            form = StoreForm()
            department_id = request.GET.get('department_id')
            courses = Courses.objects.filter(department_id=department_id).values('id', 'name')
            return JsonResponse({'courses': list(courses)})
            # return redirect('msg')
    return render(request,'form.html')
def msg(request):
    return render(request,'msg.html')

