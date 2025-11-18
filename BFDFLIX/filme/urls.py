#Ao criar uma página precisamos configurar a URL, o VIEW e o TEMPLATE.

from django.urls import path, include
from .views import homepage


urlpatterns = [
        path('', homepage)
]

# from django.contrib import path
# from.import views

# app_name = 'filme'

# urlpatterns = [
#     path('', views.homepage, name='homepage'),
# ]