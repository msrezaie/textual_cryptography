from django.shortcuts import render
from . models import Project, Profile
 

def home(request):
    projects = Project.objects.all()
    profile = Profile.objects.first()
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'projects': projects, 'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'base\home.html', context)

def project_detail(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'base\project_detail.html', {'project': projectObj, 'tags': tags})