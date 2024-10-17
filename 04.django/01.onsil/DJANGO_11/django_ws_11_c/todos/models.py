from django.db import models

# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

class Recommend(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    content = models.TextField()