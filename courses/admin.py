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
@admin.register(Quiz)
class Quiz(admin.ModelAdmin):
    list_display = ['course', 'instruction']

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=['question','question_mark', 'course']
    prepopulated_fields={'slug':('question',)}
    search_fields = ['question']

class ChoiceInline(admin.TabularInline):
    model = QuestionChoice
    
@admin.register(QuestionAnswer)
class QuestionAnswerAmin(admin.ModelAdmin):
    list_display = ['question' ,'correct_choice', 'solution' ]
# class ChoiceInline(admin.TabularInline):
#     model = 

