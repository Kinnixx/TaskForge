from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    output = ", ".join(project.name for project in projects)
    return HttpResponse(output)
