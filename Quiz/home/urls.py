from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
path('', views.home,name='home'),
path('api/get-quiz',views.get_quiz ,name='quiz')
]
