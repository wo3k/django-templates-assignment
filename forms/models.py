from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    university_id = models.BigIntegerField(unique=True)
    national_id = models.BigIntegerField()
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='students/')

    def __str__(self):
        return self.name
    