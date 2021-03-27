from django.contrib import admin
from django.urls import path, include
from student import views

urlpatterns = [
    path('', views.StudentCreateList.as_view()),
    path('<int:pk>/', views.StudentRetrieveUpdateDelete.as_view()),

]
