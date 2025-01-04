from django.shortcuts import render, redirect

from .FiletoList import Readfile, Savefile
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.timezone import now
from datetime import timedelta
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import now, make_aware
from datetime import datetime, timedelta

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
            return HttpResponseRedirect("/admin/quiz/questionsmodel/")
        else:
            form = UploadFileForm()
            return render(request, "quiz/insertQuestions.html", {"form": form})
    else:
        return redirect('/home')
def home(request):
    if not (request.user.is_authenticated):
            return redirect('/login')
    if 'quiz_questions' in request.session and 'quiz_started'  in request.session and 'submitted' in request.session  :
        del request.session['quiz_started']
        del request.session['quiz_questions']
    elif 'quiz_started'  in request.session:
        start_time_naive=datetime.strptime(request.session['quiz_started'],'%d/%m/%Y, %H:%M:%S')
        #start_time = now() - timedelta(seconds=int((now() - request.session['quiz_started'])))
        start_time = make_aware(start_time_naive)  # Make it timezone-aware

        elapsed_time = (now() - start_time).total_seconds()
        remaining_time = int(max(0, 120 - elapsed_time) ) # 120 seconds timer
        if remaining_time <= 0:
            del request.session['quiz_started']
            del request.session['quiz_questions']
            return redirect('start_quiz')  
    
    return render(request, 'quiz/home.html')

def defaultpage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    context = {
            'student': request.user.username
        }
    return render(request, 'quiz/defaultpage.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
       context={}
       return render(request,'quiz/login.html',context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/home')

    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('/login')
        context = {
            'form': form,
        }
        return render(request, 'quiz/register.html', context)

def start_quiz(request):
    if 'quiz_started' not in request.session:
        questions = list(QuestionsModel.objects.all())  # Assume Question is your model
        selected_questions = random.sample(questions, 5)  # Select 5 random questions

        # Store questions and start time in session
        request.session['quiz_questions'] = [
            {
                'id': q.id,
                'question': q.question,
                'op1': q.op1,
                'op2': q.op2,
                'op3': q.op3,
                'op4': q.op4,
            } for q in selected_questions
        ]
        request.session['quiz_started'] = datetime.strftime(now(),'%d/%m/%Y, %H:%M:%S')  # Save start time
    
    return redirect('take_quiz')
def take_quiz_view(request):
    if request.method == 'POST':
        if 'quiz_questions' in request.session and 'quiz_started'  in request.session :
            del request.session['quiz_started']
            del request.session['quiz_questions']
            request.session['submitted'] = "True"  # Save start time

        questions = QuestionsModel.objects.all()
        score = 0
        correct = 0
        wrong = 0
        total = len(questions)  # Total number of questions

        for q in questions:
            user_answer = request.POST.get(q.question)  # Ensure to use the question ID or unique key
            correct_answer = q.ans  # Assuming `ans` holds the correct answer
            print(user_answer)
            print(correct_answer)
            print()
            #if q.ans ==  request.POST.get(q.question):
            if user_answer:
                if user_answer == correct_answer:  # Case-insensitive comparison
                    score += 1  # Add points for a correct answer
                    correct += 1
                else:
                    wrong += 1
            else:
                wrong += 1  # Count unanswered questions as wrong

        #percent = (score / (total * 10)) * 100 if total > 0 else 0
        #time = request.POST.get('timer', 'N/A')  # Get the timer value from POST, default to 'N/A'

        # Assuming the username is available from the request's user (for authenticated users)
        username = request.user.username if request.user.is_authenticated else f"Student {request.user.username }"

        context = {
            'username': username,
            'score': score,
            'max_score': total ,  # Maximum score
            'total': total,
            'correct': correct,
            'wrong': wrong,
        }

        return render(request, 'quiz/result.html', context)

    else:  # For GET request, render the quiz
        if not (request.user.is_authenticated):
            return redirect('/login')
        else:
            if 'submitted' in request.session:
                del request.session['submitted']
                #return redirect('/home')
            if 'quiz_questions' not in request.session or 'quiz_started' not in request.session:
                return redirect('start_quiz')
            quiz_questions = request.session['quiz_questions']
            start_time_naive=datetime.strptime(request.session['quiz_started'],'%d/%m/%Y, %H:%M:%S')
            #start_time = now() - timedelta(seconds=int((now() - request.session['quiz_started'])))
            start_time = make_aware(start_time_naive)  # Make it timezone-aware

            elapsed_time = (now() - start_time).total_seconds()
            remaining_time = int(max(0, 120 - elapsed_time) ) # 120 seconds timer
            remaining_minutes = remaining_time // 60
            remaining_seconds = remaining_time % 60

            #if remaining_time <= 0:
                #return redirect('submit_quiz')  # Handle automatic submission

            context = {
                'questions': quiz_questions,
                'remaining_time': remaining_time,
                'remaining_minutes': remaining_minutes,
                'remaining_seconds': remaining_seconds,
                'username': request.user.username
            }
        return render(request, 'quiz/take_quiz.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/login')