from django.db import models

# Create your models here.
DIFFICULTY_CHOICES = (
    (1, 'easy'), (2, 'intermediate'), (3, 'difficult')
)


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    numberOfQuestions = models.IntegerField()
    time = models.IntegerField(help_text='Duration of quiz in minutes.')
    requiredScoredToPass = models.IntegerField(
        help_text='Required score to pass in %')
    difficulty = models.IntegerField(max_length=1, choices=DIFFICULTY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return self.name


def get_questions(self):
    return self.ques_ans_self.all()  # Need to understand this line
