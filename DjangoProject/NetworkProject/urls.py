from django.contrib import admin
from django.urls import path, include
from quiz.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insertQuestions/', insertQuestions, name='insertQuestions'),
    path('login/', loginPage, name='Login'),
    path('logout/', logoutPage,name='logout'),
  path('home/', home, name='home'),
    path('', defaultpage, name='defaultpage'),
   path('register/', registerPage,name='register'),
    path('take/', take_quiz_view, name='take_quiz'),
    path('start_quiz/', start_quiz, name='start_quiz'),

]
