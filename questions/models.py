from django.db import models
from quizes.models import Quiz
# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return str(self.text)


def get_answers(self):
    return self.answer_set.all()  # Need understand this code
