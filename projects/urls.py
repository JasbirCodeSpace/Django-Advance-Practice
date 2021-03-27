from django.contrib import admin
from django.urls import path, include
from projects import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_all'),
    path('<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('create', views.ProjectCreateView.as_view()),
    path('update/<int:pk>', views.ProjectUpdateView.as_view()),
    path('delete/<int:pk>', views.ProjectDeleteView.as_view()),
]