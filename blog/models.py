from django.db import models
from django.urls import reverse

class ToDoList(models.Model):
    id = models.AutoField(primary_key=True)
    todo = models.CharField(max_length=500)
    desc = models.TextField()
    # date_when = models.DateTimeField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo

    def get_absloute_url(self):
        return reverse('blog-home')

    def get_success_url(self):
        return reverse('blog-home')