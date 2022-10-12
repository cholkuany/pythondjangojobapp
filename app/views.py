
# from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponse, HttpResponseNotFound

from app.models import JobApp

# Create your views here.

class Temp:
    d = 500

def hello(request):
    #template = loader.get_template('app/hello.html')

    temp_object = Temp()
    list = ["garang", "deng", "majak"]

    context = {"name": "Django", "age": 34, "list_items": list, "temp_object": temp_object, "is_authenticated": False}
    #return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context)

def job_list(request):
    jobs = JobApp.objects.all()
    context = {"jobs_list": jobs}
    return render(request, "app/index.html", context)

def job_details(request, id):
    try:
        job = JobApp.objects.get(slug=id)
        context = { "job": job }
        return render(request, "app/job_details.html", context)
    except:
        return HttpResponseNotFound(f"{id} : Not Found")