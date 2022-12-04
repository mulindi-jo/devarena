from django.shortcuts import render

from projects.models import Project
from .models import Profile


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
