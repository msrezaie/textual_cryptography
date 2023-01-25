from django import forms
from django.shortcuts import render
from . models import Project, Profile, Page

class ContactForm(forms.Form):
    name = forms.CharField(label="Full Name")
    email = forms.EmailField(label="@")
    subject = forms.CharField(label="Subject")
    message = forms.CharField(label="Message", widget=forms.Textarea) 

def base(request):
    page = Page.objects.first()
    profile = Profile.objects.first()
    projects = Project.objects.all()
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'projects': projects, 'topSkills': topSkills, 'otherSkills': otherSkills, 'page': page}
    return render(request, "base/base.html", context)

def project_detail(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'base/project-detail.html', {'project': projectObj, 'tags': tags})

def contact(request):
    form = ContactForm()
    return render(request, 'base/contact-form.html', {'form': form} )