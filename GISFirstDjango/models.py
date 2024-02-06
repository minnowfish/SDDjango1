from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Students(models.Model):
    ...

class TeachingGroup(models.Model):
    student = models.ForeignKey(Students, on_delete = models.CASCADE,)
#    students = models.OneToOneField(Person, null=True, on_delete=models.SET_NULL)
