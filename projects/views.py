from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from projects.models import Project
from django.urls import reverse

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'


class ProjectCreateView(CreateView):
    model = Project
    fields = '__all__'
    template_name = 'projects/project_form.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"


class ProjectUpdateView(UpdateView):
    model = Project
    fields = '__all__'
    template_name = "projects/project_form.html"


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "projects/project_delete_confirm.html"
    def get_success_url(self):
        return reverse('project_all')





