from django.shortcuts import render, redirect
from . models import Project, Profile, Page
from . forms import ContactForm


def base(request):
    page = Page.objects.first()
    profile = Profile.objects.first()
    projects = Project.objects.all()
    
    # topSkills = profile.skill_set.exclude(description__exact="")
    # otherSkills = profile.skill_set.filter(description="")

    form = ContactForm(request.POST or None)
    form_message = ""

    if request.method == 'POST' and form.is_valid():
        form.save()
        form_message = "Thank you for contacting, I will get back to you ASAP!"

    context = {
        'profile': profile,
        'projects': projects,
        'page': page,
        'form': form,
        'form_message': form_message,
    }
    
    return render(request, "base/base.html", context)

def project_detail(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'base/project-detail.html', {'project': projectObj, 'tags': tags})
