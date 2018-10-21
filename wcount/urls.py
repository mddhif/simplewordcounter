from django.urls import path
from django.conf.urls import url

from wcount import views



urlpatterns = [

url(r'^wcount/', views.wordcount, name="wordcounter"),

url(r'^jquery/', views.jquery, name="jquery"),
]