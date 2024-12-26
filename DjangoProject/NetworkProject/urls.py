from django.contrib import admin
from django.urls import path, include
from quiz.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insertQuestions/', insertQuestions, name='insertQuestions'),
    path('login/', loginPage, name='Login'),
    path('logout/', logoutPage,name='logout'),
  path('home', home, name='home'),
   path('register/', registerPage,name='register'),
    path('take/<str:student_id>/', take_quiz_view, name='take_quiz'),

]
