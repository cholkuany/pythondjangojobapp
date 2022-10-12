from django.urls import path
from uploadapp import views

urlpatterns = [
    path('image/', views.upload_image, name='upload_image'),
    path('file/', views.uploadFile, name='upload_file'),
]