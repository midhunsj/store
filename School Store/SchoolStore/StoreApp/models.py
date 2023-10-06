from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name=models.CharField(max_length=50)
    course=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

