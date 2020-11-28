from django.contrib import admin
from courses.models import *
# from .models import Question, Choice
# from .forms import QuestionForm, ChoiceForm, ChoiceInlineFormset



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    
    
@admin.register(Courses)

class CoursesAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
    
# Register your models here.


@admin.register(QuizProfile)
class QuizProfileAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','total_score']

@admin.register(Question)
class QuizProfileAdmin(admin.ModelAdmin):
        list_display =['question', 'course', 'question_mark']



@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display=['question', 'correct_option', 'solution', 'answer_marks']
