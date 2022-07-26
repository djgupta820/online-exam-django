from django.db import models
# Create your models here.
   

class all_students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    roll_number = models.BigIntegerField()
    course = models.CharField(max_length=100)
    semester = models.IntegerField()
    joined = models.DateField()
    password = models.CharField(max_length=20, default='user12345')
    registered_at = models.DateTimeField(auto_now_add=True)

