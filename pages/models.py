from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    university_id = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    address = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.full_name
