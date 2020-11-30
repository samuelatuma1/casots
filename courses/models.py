from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils.models import TimeStampedModel
import random
from django.db.models import F, Q, Count, Sum, Case, When
from django.db.models.functions import Cast
from django.utils.translation import gettext as _
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200 ,unique=True)
    
    class Meta:
        ordering=('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    category = models.ForeignKey(Category, related_name = 'courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=250,)
    body = models.TextField()
    description =RichTextField()
    slug=models.SlugField(max_length=250,unique=True)
    images = models.ImageField(upload_to='courses/',blank=True, null=True)
    
    class Meta:
        ordering=('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'
   
    def get_absolute_url(self):
        return reverse('courses:course_summary',
                       args = [self.slug])
    
    def __str__(self):
        return self.name
    
# my code  

#quiz profiles for users
class QuizProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    total_score = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
    def __str__(self):
        return f'{first_name} {last_name}'
    
    
# Quiz for instruction 
class Quiz(models.Model):
    course=models.ForeignKey(Courses ,on_delete=models.CASCADE)
    slug = models.SlugField()
    description=models.TextField(blank=True, null=True)
    instruction = RichTextField()
    
    def __str__(self):
        return self.course

# quiz questions
class QuizQuestion(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.TextField()
    question_mark = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.question

# question choice
class QuestionChoice(models.Model):
    question =models.ForeignKey(QuizQuestion,on_delete=models.CASCADE)
    option = models.TextField()
    is_correct = models.BooleanField(default=False)

# quiz answers
class QuestionAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    correct_choice = models.ForeignKey(QuestionChoice, max_length=20 ,on_delete=models.CASCADE)
    answer_marks = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    solution = models.TextField()