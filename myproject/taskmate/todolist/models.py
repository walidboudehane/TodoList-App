from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=200)
    done=models.BooleanField(default=False)
    
    def __str__(self):
        return self.task + '-'+str(self.done)


    