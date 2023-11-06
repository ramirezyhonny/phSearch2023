from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User, userPhotographer
from django.db import IntegrityError
#propio formulario
from .forms import CustomUserCreationForm
#edit profile
from .forms import editProfile
#search_profile

from django.db.models import Q

# Create your views here.
def home(request):
    username=request.user.username;
    return render(request, 'home.html',{
        'username':username
    })
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                email=request.POST['email'],
                                                password=request.POST['password1'],
                                                country=request.POST['country'],
                                                provinces=request.POST['provinces'],
                                                usertype=request.POST['usertype']
                                                )
                if 'picture' in request.FILES:
                    user.picture = request.FILES['picture']  # Asignar imagen de perfil si se proporciona

                if request.POST['usertype'] == 'photographer':
                    photographer=userPhotographer(user=user)
                    photographer.save()
                login(request,user)
                user.save()
                return redirect('userclient')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': CustomUserCreationForm,
                    'error': "user already exists"
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': "password do not match"
        })
#def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user = form.save(commit=False)
                    user.set_password(form.cleaned_data['password1'])
                    user.picture = form.cleaned_data['picture']
                    user.save()
                    login(request, user)
                    return redirect('userclient')
                except IntegrityError:
                    return render(request, 'signup.html', {
                        'form': CustomUserCreationForm,
                        'error': "El usuario ya existe"
                    })
            else:
                return render(request, 'signup.html', {
                    'form': CustomUserCreationForm,
                    'error': "Las contraseñas no coinciden"
                })
        else:
            return render(request, 'signup.html', {
                'form': CustomUserCreationForm,
                'error': "Error en el formulario"
            })
    else:
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm
        })
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': "Username or password is incorrect"
            })
        else:
            login(request,user)
            return redirect('home')

def signout(request):
    logout(request)
    return redirect('home')

def userclient(request):
    return render(request, 'userclient.html')
def about(request):
    username=request.user.username;
    first_name=request.user.first_name;
    last_name=request.user.last_name;
    email=request.user.email;
    return render(request, 'about.html',{
        'username':username,
        'first_name':first_name,
        'last_name':last_name,
        'email':email
    })
def myprofile(request):
    username=request.user.username;
    first_name=request.user.first_name;
    last_name=request.user.last_name;
    email=request.user.email;
    return render(request, 'myprofile.html',{
        'username':username,
        'first_name':first_name,
        'last_name':last_name,
        'email':email
    })
def edit_profile(request):
    username=request.user.username;
    first_name=request.user.first_name;
    last_name=request.user.last_name;
    email=request.user.email;
    country=request.user.country;
    provinces=request.user.provinces;
    if request.method == 'POST':
        form=editProfile(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('myprofile')
    else:
        initial_data = {
            'country': request.user.country,  # Establece el valor inicial para 'country'
            'provinces': request.user.provinces,  # Establece el valor inicial para 'provinces'
        }
        form = editProfile(instance=request.user, initial=initial_data)
    return render(request, 'setting_profile.html', {
        'form':form,
        'username':username,
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'country':country,
        'provinces':provinces,
        })
    
def search(request):
    query = request.GET.get('q','')
    users=[]
    if query:
        users =  User.objects.filter(first_name__icontains=query)
    return render(request, 'search.html', {
        'users': users,
        'query': query
    })
def avance_search(request):
    users = []  # Inicialmente, establecemos una lista vacía de usuarios.
    if request.method == 'GET':
        query_username = request.GET.get('username', '').strip()
        query_email = request.GET.get('email', '').strip()
        query_country = request.GET.get('country','').strip()
        query_provinces = request.GET.get('provinces','').strip()
        query_specialty = request.GET.get('specialty','').strip()

        if query_username or query_email or query_country or query_provinces or query_specialty:
            # Si se proporcionaron parámetros de búsqueda, realizamos la consulta.
            users = User.objects.all()  # Consulta inicial que incluye a todos los usuarios.
            if query_username:
                users = users.filter(username__icontains=query_username)
            if query_email:
                users = users.filter(email__icontains=query_email)
            if query_country:
                users = users.filter(country__icontains=query_country)
            if query_provinces:
                users = users.filter(provinces__icontains=query_provinces)
            if query_specialty:
                users=users.filter(specialty__icontains=query_specialty)
        else:
            users=[];
        no_results= not users
        users_list=list(users);
        cant_results=len(users_list);
        if cant_results>1:
            cant_text='results found';
        elif cant_results==1:
            cant_text='result found';
        else:
            cant_text='No result found'
    return render(request, 'avance_search.html', {
        'users': users,
        'no_results':no_results,
        'cant_results':cant_results,
        'cant_text':cant_text
    })
