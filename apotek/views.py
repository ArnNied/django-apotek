from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
# from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.core.validators import validate_email
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
    # print(request.session.items())
    context = {
        'page_title': "Apotek",
    }
    return render(request, 'apotek/index.html', context)

def user_landing(request):
    if '_auth_user_hash' in request.session:
        return redirect('apotek:index')

    else:
        context = {
            'page_title': "Apotek",
            'login_form': LoginForm(),
            'register_form': RegisterForm()
        }
        return render(request, 'apotek/user_landing.html', context)

def user_login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        # user = authenticate(username=request.POST['username'], password=request.POST['password'])
        
        # if user is not None:
        #     login(request, user)
        #     return redirect('/')
        # else:
        #     form.add_error('username', 'Username or password incorrect')
        #     form.add_error('password', 'Username or password incorrect')

        try:
            user = User.objects.get(username=request.POST['username'])
            if not check_password(request.POST['password'], user.password):
                form.add_error('password', 'Incorrect password')
        except ObjectDoesNotExist:
            form.add_error('username', 'User does not exist')
        
        if form.errors:
            context = {
                'login_error': form.errors,
                'page_title': "Apotek",
                'login_form': LoginForm(),
                'register_form': RegisterForm()
            }

            return render(request, 'apotek/user_landing.html', context)
        else:
            login(request, user)
            if user.is_staff == True:
                request.session['staff'] = True
            return redirect('/')

    else:
        redirect('/')
def user_register(request):
    if request.method == 'POST':
        
        data = request.POST.copy()
        data['password'] = make_password(data['password'])
        
        form = RegisterForm(data)
        form.is_valid()

        try:
            if request.POST['password'] != request.POST['conpassword']:
                form.add_error('conpassword', 'Password do not match')
        except KeyError:
            pass
            
        if form.errors:
            context = {
                'page_title': 'Apotek',
                'register_error': form.errors,
                'login_form': LoginForm(),
                'register_form': RegisterForm()
            }
            return render(request, 'apotek/user_landing.html', context)
            
        else:
            form.save()
        
            user = User.objects.get(username=data['username'])
            login(request, user)
            
            return redirect('/')
    else:
        return redirect('apotek:index')

def user_logout(request):
    logout(request)

    return redirect('/user/landing/')