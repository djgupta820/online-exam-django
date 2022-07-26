from django.contrib import admin
from .models import all_courses
from .models import exams, t_profile

# Register your models here.

admin.site.register(all_courses)
admin.site.register(exams)
admin.site.register(t_profile)