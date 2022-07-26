from django.db import models

# Create your models here.

class all_courses(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    started_year = models.DateField()

class t_profile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    username = models.CharField(max_length=100, default="na")
    mobile_number = models.BigIntegerField()
    address = models.CharField(max_length=100)
    employment_number = models.CharField(max_length=25)
    designation = models.CharField(max_length=25)


class exams(models.Model):
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=10)
    subject = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=10)
    date_of_exam = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    scheduled_by = models.CharField(max_length=50)
    question_file = models.FileField(default='file')
    answer_file = models.FileField(default='file')
