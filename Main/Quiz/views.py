from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
#from .forms import *
from .FiletoList import*
from .models import *
from django.http import HttpResponse
import os
# Create your views here.
def insertQuestions(request):
    questions ={}
    if(request.method =='POST'):
         
        # Iterate through all the data items
        for field, data in request.files.items():
            print('field:', field)
            print('filename:', data.filename)
            if data.filename:
                data.save(os.path.join('media', data.filename))
                questions=Readfile(data.filename)
            for ques in questions:
                # Insert in the database
                QuestionsModel.objects.create(question = ques["Question_statement"], op1 = ques["A"],op2 = ques["B"],op3 = ques["C"],op4 = ques["D"],ans=ques["Correct Answer"])
            return redirect('/')
    context = { }
    # Returning the rendered html
    return render(request, "Quiz/insertQuestions.html", context)
