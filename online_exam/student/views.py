from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import all_students
from teacher.models import all_courses, exams
import datetime 

# Create your views here.

def student_index(request):
    return render(request, 'st_index.html')

def student_login(request):
    return render(request, 'student_login.html')

def student_login_function(request):
    if request.method == 'POST':
        stud = all_students.objects.get(roll_number=request.POST['username'])
        allExams = exams.objects.all()
        #allExams = exams.objects.filter(date_of_exam=datetime.date.today())
        if stud:
            if stud.roll_number == int(request.POST['username']) and stud.password == request.POST['password']:
                request.session['stuname'] = request.POST['username']          # set session
                request.session['stpasswd'] = request.POST['password']
                msg = ""
                context = {
                    'message':msg, 
                    'student':stud, 
                    "exams":allExams
                    }
                return render(request, 'waiting_area.html', context)
            else:
                msg = "Invalid Credentials. The credentials could be case sensitive"
                return render(request, 'student_login.html', {"message":msg})        
        else:
            msg = "Invalid credentials"
            return redirect('student_login')
    else:
        return redirect('student_login')

def waiting_area(request):
    allExams = exams.objects.all()
    #allExams = exams.objects.filter(date_of_exam=datetime.date.today())
    context = {
        "exams":allExams
    }
    return render(request, 'waiting_area.html', context)

def register(request):
    all_c = all_courses.objects.all()
    sems = []
    for i in range(1, 9):
        sems.append(i)
    
    context = {"courses":all_c, "sems":sems}
    return render(request, 'register.html', context)

def registration(request):
    if request.method == 'POST':
        all_studs = all_students.objects.filter(roll_number=request.POST['roll_number'])
        if request.POST['password1'] != request.POST['password2']:
            all_c = all_courses.objects.all()
            sems = []
            for i in range(1, 9):
                sems.append(i)
            
            msg = "Error: Password Mismatch"
            context = {"courses":all_c, "sems":sems, 'errors':msg}
            return render(request, 'register.html', context)

        elif all_studs:
            all_c = all_courses.objects.all()
            sems = []
            for i in range(1, 9):
                sems.append(i)
            
            msg = "Student Exist with Roll Number:" + request.POST['roll_number']
            context = {"courses":all_c, "sems":sems, 'errors':msg}
            return render(request, 'register.html', context)

        else:
            s = all_students(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], roll_number = request.POST['roll_number'], course=request.POST['course'], semester=request.POST['semester'], joined=request.POST['joined'], password=request.POST['password1'])
            s.save()
        return redirect('student_login')
    else:
        msg = "Error"
        return render(request, 'register.html', {'errors':msg})

def student_profile(request):
    stud = all_students.objects.get(roll_number=request.session['stuname'])
    context = {
        'student': stud
    }
    return render(request, 'st_profile.html', context)

def student_logout(request):
    try:
        del request.session['username']
        msg = "Session Destroyed"
    except KeyError:
        msg = KeyError
    return render(request, 'logout.html', {"message":msg})