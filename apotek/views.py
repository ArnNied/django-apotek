from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, SearchForm
from .models import Product
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.cache import caches
from math import ceil

# Create your views here.

@login_required
def index(request, page=1, query=''):
    try:
        query = request.GET['search']
        products = Product.objects.filter(Q(name__icontains=query) | Q(tags__icontains=query))
    except KeyError:
        products = Product.objects.all()

    paginator = Paginator(products, 2, allow_empty_first_page=True)
    page = paginator.page(page)
    
    context = {
        'page_title': "Apotek",
        'products': page,
        'search': SearchForm()
    }

    return render(request, 'apotek/index.html', context)


def user_auth(request):
    if '_auth_user_hash' in request.session:
        return redirect('apotek:index')

    else:
        context = {
            'page_title': "Apotek",
            'login_form': LoginForm(),
            'register_form': RegisterForm(),
        }

        if 'login' in request.POST:

            login_form = LoginForm(request.POST)

            try:
                user = User.objects.get(username=request.POST['username'])
                if not check_password(request.POST['password'], user.password):
                    login_form.add_error('password', 'Incorrect password')
            except ObjectDoesNotExist:
                login_form.add_error('username', 'User does not exist')

            if login_form.errors:
                context['login_error'] = login_form.errors
            else:
                login(request, user)
                if user.is_staff == True:
                    request.session['staff'] = True
                return redirect('apotek:index')

        if 'register' in request.POST:
            
            data = request.POST.copy()
            data['password'] = make_password(data['password'])
            
            register = RegisterForm(data)
            register.is_valid()

            try:
                if request.POST['password'] != request.POST['conpassword']:
                    register.add_error('conpassword', 'Password do not match')
            except KeyError:
                pass
                
            if register.errors:
                context['register_error'] = register.errors
            else:
                register.save()
                user = User.objects.get(username=data['username'])
                login(request, user)

                return redirect('apotek:index')

        return render(request, 'apotek/user_landing.html', context)

def user_logout(request):
    logout(request)

    return redirect('apotek:index')

# def upload(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['file']

#     return render(request, 'apotek/upload.html')