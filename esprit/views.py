from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from  .models import Project
def helloDjango(request):
    return  HttpResponse("Bonjour Django")
def detail(request , id):
    return HttpResponse("Bonjour %s "%id)
def getAll(request):
    projects = Project.objects.all()
    return  render(request ,'list_projet.html',{'p':projects})