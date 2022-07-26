from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='teacher-index'),                                                                #working
    path('login/', LoginView.as_view(), {'template_name':'login.html'}, name='login'),                          #working
    path('dashboard/', views.dashboard, name='dashboard'),                                                      #working
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),             #working
    path('students/', views.students, name='students'),                                                         #working
    path('courses/', views.courses, name='courses'),                                                            #working
    path('exams/', views.exams, name='exams'),                                                                  #working
    path('schedule-exam/', views.scheduleExam, name='scheduleExam'),                                            #working
    path('profile/', views.profile, name='profile'),                                                            #working
    path('schedule', views.schedule, name='schedule'),                                                          #working
    path('calender/', views.calender, name='calender'),                                                         #working
    path('search_student_by_name/', views.search_student_by_name, name='search_st_name'),                       #working
    path('search_student_by_roll_number/', views.search_student_by_roll_number, name='search_st_roll_no'),      #working
    path('search_exam_by_name', views.search_exam_by_name, name="search_exam_by_name"),                         #working
    path('question-paper/', views.question_paper, name='question_paper'),
    path('test/', views.test, name='test'),
]
