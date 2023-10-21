from django.db import models

# Create your models here.
class Questions(models.Model):
    id_questions = models.TextField(blank=True)
    text = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    time_create = models.DateTimeField(blank=True)

    def __str__(self):

        return self.id_questions