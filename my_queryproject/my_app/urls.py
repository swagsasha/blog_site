from django.urls import path
from . import views

urlpatterns = [
    # Укажите функцию отображения, которая у вас написана в views.py
    path('', views.post_list, name='post_list'),
]
