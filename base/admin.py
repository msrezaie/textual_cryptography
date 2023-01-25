from django.contrib import admin
from . models import Project, Tag, Profile, Skill, Page

admin.site.register(Page)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Skill)