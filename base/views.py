from django.shortcuts import render, redirect
from . models import Project, Profile, Page
from . forms import ContactForm

def base(request):
    page = Page.objects.first()
    profile = Profile.objects.first()
    projects = Project.objects.all()
    
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')

    context = {
        'profile': profile,
        'projects': projects,
        'topSkills': topSkills,
        'otherSkills': otherSkills,
        'page': page,
        'form': form
    }
    
    return render(request, "base/base.html", context)

def project_detail(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'base/project-detail.html', {'project': projectObj, 'tags': tags})
