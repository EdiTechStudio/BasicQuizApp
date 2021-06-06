from django.db import models

# Create your models here.
DIFFICULTY_CHOICES = (
    ('Easy', 'Easy'),
    ('Intermediate', 'Intermediate'),
    ('Difficult', 'Difficult'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_Of_Questions = models.IntegerField()
    time = models.IntegerField(help_text='Duration of quiz in minutes.')
    required_Score_To_Pass = models.IntegerField(
        help_text='Required score to pass in %')
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return self.name


def get_questions(self):
    # Need to understand this line
    return self.ques_ans_self.all()[:self.number_Of_Questions]
# Simple change
