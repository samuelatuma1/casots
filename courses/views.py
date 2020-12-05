from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from courses.models import Courses,Category
from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from .models import QuizProfile, QuizQuestion,QuestionAnswer,QuestionChoice,Quiz
from django.http import Http404
from django.contrib.auth.decorators import login_required


#home page 

def home(request):
    context={}
    return render(request, 'courses/index.html',context)

# about page
def about(request):
    context={}
    return render(request, 'courses/about.html', context)

# all the courses page
def courses_list(request, category_slug=None):
    category =None
    courses = Courses.objects.all()
    if category_slug:
        category = Category.objects.get(slug = category_slug )
        courses =  courses.filter(category=category)
    paginator = Paginator(courses, 4)
    page_number=request.GET.get('page')
    courses = paginator.get_page(page_number)
    
    context = {'course':courses}
    return render(request, 'courses/course_list.html', context)


# summary of each course
def course_summary(request, course_slug):
    courses = Courses.objects.get(slug=course_slug)
    context = {'courses':courses}
    return render(request, 'courses/course_summary.html', context)

# logout page
def logout_view(request):
    logout(request)
    return redirect("/login")

# register page
def register(request):
    form = RegistrationForm(request.POST)     
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login')

    context = {'form': form}
    return render(request, 'courses/registration/sign_up.html', context=context)

# login page
def login_view(request):
    form =UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/dashboard')
    return render(request, 'courses/registration/sign_up.html', {"form": form})

@login_required
def dashboard(request):
    return render(request,'quiz/user_dashboard.html')


@login_required 
def quiz_instruction(request, instruction_slug):
    return render(request, 'quiz/quiz_instructions.html', context)

@login_required
def quiz(request,quiz_slug,):
    quiz= QuizQuestion.objects.get(slug=quiz_slug)
    context = {'quiz':quiz,'quiz_answer':quiz_answer}
    return render(request, 'quiz/quiz.html',context)

@login_required
def quiz_choice(request,choice_slug):
    quiz_choice = QuizChoice.objects.get(slug= choice_slug)
    context = {'quiz_choice':quiz_choice}
    return render(request, 'quiz/quiz.html', context)

@login_required
def quiz_answer(request,answer_slug):
    quiz_answer = QuizAnswer.objects.get(slug=answer_slug)
    context = {'quiz_answer':quiz_answer}
    return render(request,'quiz/quiz.html',context)

def leaderboard(request):
    return render(request, 'quiz/leaderboard.html', context=context)
