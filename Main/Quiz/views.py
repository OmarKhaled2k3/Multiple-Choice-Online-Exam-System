from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
#from .forms import *
from .FiletoList import*
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import os.path
# Create your views here.
def insertQuestions(request):
    if request.user.is_staff:
        if request.method == "POST" :
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                f= request.FILES['file']
                Savefile(f)
                questions=Readfile(f.name)
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
