# Create  Student Model and  Course Model
from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=30)
    marks = models.IntegerField()
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.sname


class Course(models.Model):
    cname = models.CharField(max_length=30)
    cfee = models.IntegerField()

    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.cname
