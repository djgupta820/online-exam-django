from django.urls import URLPattern, path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.student_index, name='student_index'),
    path('student-login/', views.student_login, name='student_login'),
    path('student-dashboard/', views.waiting_area, name='waiting_area'),
    path('student_login_function', views.student_login_function, name='stud_login'),
    path('register/', views.register, name="register"),
    path('registration', views.registration, name='registration'),
    path('student-profile/', views.student_profile, name='student_profile'),
    path('student-logout', views.student_logout, name='student_logout'),
]