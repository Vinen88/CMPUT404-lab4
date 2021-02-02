from django.urls import path
from . import views

#this gets consulted only if the url starts with baseurl+/polls/
urlpatterns = [
  path('', views.index, name='index')
]