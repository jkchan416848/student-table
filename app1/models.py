from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    Name = models.CharField(max_length=20)
    Roll_no = models.IntegerField()
    Phone_no = models.PositiveBigIntegerField()
    Standard = models.IntegerField()
    Tamil = models.IntegerField()
    English = models.IntegerField()
    Maths = models.IntegerField()
    Science = models.IntegerField()
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()


