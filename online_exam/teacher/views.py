from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.conf import settings 
from .models import all_courses, t_profile
from .models import exams as ex
from student.models import all_students
import datetime
import json

def test(request):
    now = datetime.datetime.now()
    exam = ex.objects.get(date_of_exam=now.strftime('%Y-%m-%d'))
    filename = settings.MEDIA_ROOT + '\\' + str(exam.question_file)
    '''file = []
    try:
        f = open(filename, 'r')
        for line in f:
            if line[0].isnumeric():
                q.append(line)
            else:
                an.append(line)
    except:
        print("error")
    
    var = json.dumps({qn,an})
    
    for _ in range(len(qn)):
        pass
    '''

    arr = []
    f = open(filename, 'r')
    for line in f:
        arr.append(line)
    
    context = {
        "arr":arr,
    }
    #JsonResponse()
    return render(request,'test.html', context)


def index(request):
    return render(request, 'index.html')

def logout(request):
    logout(request)


def dashboard(request):
    usr = t_profile.objects.get(username = request.user)
    return render(request, 'dashboard.html', {'det':usr})


def students(request):
    ast = all_students.objects.all()
    return render(request, 'students.html', {"students":ast})


def profile(request):
    usr = t_profile.objects.get(username = request.user)
    return render(request, 'profile.html', {'user':usr})
    

def scheduleExam(request):
    return render(request, 'scheduleExam.html')


def schedule(request):
    if request.method == 'POST':
        cn = request.POST['course']
        sem = request.POST['semester']
        subj = request.POST['subject']
        subj_code = request.POST['subject_code']
        date_exam = request.POST['date_of_exam']
        stime = request.POST['start_time']
        etime = request.POST['end_time']
        scheduled = request.user
        file1 = request.FILES['ques_file']
        print(file1)
        file2 = request.FILES['ans_file']
        e = ex(course=cn, semester=sem, subject=subj, subject_code=subj_code, date_of_exam=date_exam, start_time=stime, end_time=etime, scheduled_by=scheduled, question_file=file1, answer_file=file2)
        e.save()
        return redirect('dashboard')
        
    else:
        msg = "error scheduling exam"
        redirect('scheduleExam', {'error':msg})

def exams(request):
    now = datetime.datetime.now()
    nd = now.strftime("%Y-%m-%d")
    nt = now.strftime("%I:%M %p")
    exm = ex.objects.all()
    return render(request, 'exams.html', {'exams':exm, "time":nt, "date":nd})


def courses(request):
    css = all_courses.objects.all() 
    return render(request, 'courses.html', {"courses":css})


def calender(request):
    return render(request, 'calender.html')


def search_student_by_name(request):
    query = request.GET['query'].capitalize() 
    all_st = all_students.objects.filter(first_name=query)
    context = {
        'students':all_st, 
        'query':query, 
        'lenth':len(all_st),
        'st':'st'
    }
    return render(request, 'search.html', context)


def search_student_by_roll_number(request):
    query = request.GET['query']
    all_st = all_students.objects.filter(roll_number=query)
    context = {
        'students':all_st, 
        'query':query, 
        'lenth':len(all_st),
        'st':'st'
    }
    return render(request, 'search.html', context)

def search_exam_by_name(request):
    query = request.GET['query']
    all_e = ex.objects.filter(scheduled_by=query)
    context = {
        'exams':all_e, 
        'query':query, 
        'lenth':len(all_e),
        'st':'exam'
    }
    return render(request, 'search_ex.html', context)


def question_paper(request):
    # now = datetime.datetime.now()
    # t = now.strftime('%Y-%m-%d')
    ques_paper = request.GET['ques_file']
    exam = ex.objects.get(date_of_exam=ques_paper)
    filename = settings.MEDIA_ROOT + '\\' + str(exam.question_file)
    ques = []

    try:
        file = open(filename, 'r')
        for line in file:
            ques.append(line)

        context = {
            'q':ques,
        }
        #print('file found')
    except:
        print("Error")
    return render(request, 'question_paper.html', context)
