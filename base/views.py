from django.shortcuts import render
from . models import Project, Profile
 

def home(request):
    profile = Profile.objects.first()
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, "base/landing.html", context)

def portfolio(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, "base/projects.html", context)

def project_detail(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'base\project_detail.html', {'project': projectObj, 'tags': tags})
