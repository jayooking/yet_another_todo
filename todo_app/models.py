from django.db import models
# from djongo import models
# from collections import MutableMapping

# Create your models here.
class Task(models.Model):
    '''Creating the task table in my database'''
    name = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.name
    #    , self.id, self.date_created

class Meta:
    ordering = ['-id']