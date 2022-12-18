from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from projects.models import Project
from .models import Profile
from .forms import CustomUserCreationForm


def login_user(request):
    page = 'login'
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('developers')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('developers')
        else:
            messages.error(request, 'Username or password is not correct')
    return render(request, 'users/login_register.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'User successfully logout.')
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Account successfully created')

            login(request, user)
            return redirect('developers')
        else:
            messages.error(request, 'An error occurred during registration, please try again')
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def developers(request):
    profiles = Profile.objects.filter(is_deleted=False, is_archived=False)
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def developer(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description='')
    projects = Project.objects.filter(project_owner=pk)
    context = {'profile': profile, 'top_skills': top_skills, 'other_skills': other_skills, 'projects': projects}
    return render(request, 'users/profile.html', context)
