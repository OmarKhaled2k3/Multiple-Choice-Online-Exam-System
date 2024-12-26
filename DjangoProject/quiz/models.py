from django.db import models
import random

class QuestionsModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.text

    def grade_quiz(self, answers):
        score = 0
        for i, question in enumerate(self.questions.all()):
            if answers.get(str(question.id)) == question.correct_answer:
                score += 1
        return score
