from django.db import models

# Create your models here.
class Student(models.Model):
    # need to provide all the students properties and parameters
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()


    def __str__(self):
        # returns a str rep of object
        # applies to python classes in general
        # added to a model to provide a human readable version of hte model in django admin

        return f'Student: {self.first_name} {self.last_name}'
