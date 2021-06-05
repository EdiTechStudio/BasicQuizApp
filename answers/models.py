from django.db import models
from questions.models import Question
# Create your models here.


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"question:{self.question.text}, answer: {self.text}, correct: {self.correct}"
