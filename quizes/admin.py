from django.contrib import admin
from .models import Quiz
# Register your models here.


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'difficulty', 'created')


admin.site.register(Quiz, QuizAdmin)
