from . import views
from django.urls import path

app_name = 'Poll'

urlpatterns = [
    path('App/', views.poll, name='poll'),
    path('Save/', views.save, name='save'),
]