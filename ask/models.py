from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.TextField(blank=True, null=True)
    question = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name + '\'s Question'
