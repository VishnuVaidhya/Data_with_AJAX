from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to='images/', blank=True)
    enroll_number = models.IntegerField()
    gender = models.CharField(max_length=60)
    hobbies = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name