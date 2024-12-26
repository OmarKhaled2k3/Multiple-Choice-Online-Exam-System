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
            return HttpResponseRedirect("quiz/take/")
        else:
            form = UploadFileForm()
            return render(request, "quiz/insertQuestions.html", {"form": form})
    else:
        return redirect('home')
def home(request):
    return render(request, 'quiz/home.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
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

from django.shortcuts import render, redirect

def take_quiz_view(request, student_id):
    if request.method == 'POST':
        questions = QuestionsModel.objects.all()
        score = 0
        correct = 0
        wrong = 0
        total = len(questions)  # Total number of questions

        for q in questions:
            user_answer = request.POST.get(str(q.id))  # Ensure to use the question ID or unique key
            correct_answer = q.ans  # Assuming `ans` holds the correct answer

            if user_answer:
                if user_answer.strip().lower() == correct_answer.strip().lower():  # Case-insensitive comparison
                    score += 10  # Add points for a correct answer
                    correct += 1
                else:
                    wrong += 1
            else:
                wrong += 1  # Count unanswered questions as wrong

        percent = (score / (total * 10)) * 100 if total > 0 else 0
        time = request.POST.get('timer', 'N/A')  # Get the timer value from POST, default to 'N/A'

        # Assuming the username is available from the request's user (for authenticated users)
        username = request.user.username if request.user.is_authenticated else f"Student {student_id}"

        context = {
            'username': username,
            'score': score,
            'max_score': total * 10,  # Maximum score
            'total': total,
            'correct': correct,
            'wrong': wrong,
            'time': time,
            'percent': percent,
        }

        return render(request, 'quiz/result.html', context)

    else:  # For GET request, render the quiz
        questions = QuestionsModel.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'quiz/take_quiz.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')