from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.vault_list),
    path('add_password', add_password, name='add_password'),
]