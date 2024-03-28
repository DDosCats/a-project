from django.urls import path
from . import views

app_name = 'setings'

urlpatterns = [
    path('', views.index, name='index'),
]
