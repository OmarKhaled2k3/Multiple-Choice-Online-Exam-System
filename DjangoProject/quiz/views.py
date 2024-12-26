from django.shortcuts import render, redirect

from .FiletoList import Readfile, Savefile
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
import json
import time


def insertQuestions(request):
    if request.user.is_staff:
        if request.method == "POST" :
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                f= request.FILES['file']
                Savefile(f)
                questions=Readfile()
                QuestionsModel.objects.all().delete()
                for ques in questions:
                    # Insert in the database
                    QuestionsModel.objects.create(question = questions[ques]["Question Statement"], op1 = questions[ques]["A"],op2 = questions[ques]["B"],op3 = questions[ques]["C"],op4 = questions[ques]["D"],ans=questions[ques]["Correct Answer"])
            return HttpResponseRedirect("/admin/Quiz/questionsmodel/")
        else:
            form = UploadFileForm()
            return render(request, "Quiz/insertQuestions.html", {"form": form})
    else:
        return redirect('home')
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuestionsModel().objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz/result.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('generate_quiz')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'quiz/login.html',context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'quiz/register.html', context)

def take_quiz_view(request, student_id):
    '''
    if request.method == 'POST':
        quiz = QuestionsModel.objects.all()
        answers = request.POST
        score = quiz.grade_quiz(answers)
        return render(request, 'quiz/result.html', {'score': score, 'student_id':student_id})
    '''
    if request.method == 'POST':
        print(request.POST)
        questions=QuestionsModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz/result.html',context)
    else:
        questions = QuestionsModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request, 'quiz/take_quiz.html', context)

def logoutPage(request):
    logout(request)
    return redirect('/')