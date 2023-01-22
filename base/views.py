from django.shortcuts import render
from . models import Project, Profile
 

def index(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'projects': projects, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, "base/index.html", context)

def project_detail(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'base/project_detail.html', {'project': projectObj, 'tags': tags})