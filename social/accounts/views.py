from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm, ProfileForm
# Create your views here.
def profile(req):
    try:
        context = {
            'current_user': User.objects.get(is_current_user=True)
        }
    except:
        context = {
            'current_user': None
        }
    return render(req, 'profile.html', context)

def user_details(req, id):
    context = {
        'users': User.objects.get(id=id)
    }
    return render(req, 'user_details.html', context)

def register_user(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        age = req.POST.get('age')
        email = req.POST.get('email')
        password = req.POST.get('password')

        new_user = User(username=username, age=age,email=email, password=password, is_current_user=False)
        new_user.save()
    context = {
        'register_form': RegisterForm()
    }
    return render(req, 'register.html', context)

def login_user(req):
    if req.method == 'POST':
        found_user = User.objects.get(email=req.POST.get('email'), password=req.POST.get('password'))
        
        User.objects.update(is_current_user=False)
        
        found_user.is_current_user = True
        found_user.save()
        return redirect('profile')
    context = {
        'login_form': LoginForm()
    }
    return render(req, 'login.html', context)

def profile_edit(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        age = req.POST.get('age')
        email = req.POST.get('email')
        password = req.POST.get('password')

        current_user = User.objects.get(is_current_user=True)

        current_user.username = username
        current_user.age = age
        current_user.email = email
        current_user.password = password
        current_user.save()
        return redirect('profile')
    context = {
        'profile_form': ProfileForm()
    }
    return render(req, 'profile_edit.html', context)