from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('about/', views.about),
]