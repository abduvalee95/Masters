from django.urls import path
from .views import form

urlpatterns = [
    path('info/', form, name='info' )
]