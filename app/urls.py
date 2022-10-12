from django.urls import path

from app import views

urlpatterns = [
    path('', views.job_list, name="home"),
    path('hello', views.hello, name="hello"),
    path('job/<slug:id>', views.job_details, name="job_details"),
]