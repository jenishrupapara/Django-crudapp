from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=4)
    sname = models.CharField(max_length=255)
    scontact =models.CharField(max_length=15)
    
    
    def _str_(self):
        return self.sname
        
    
    