from django.db import models
from student.models import Student
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length = 50)
    link = models.URLField(max_length = 200, unique=True)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
