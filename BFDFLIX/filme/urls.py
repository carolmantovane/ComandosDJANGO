from django.contrib import path
from.import views

app_name = 'filme'

urlpatterns = [
    path('', views.homepage, name='homepage'),
]