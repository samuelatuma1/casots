from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from courses.models import Courses,Category
from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from .models import QuizProfile, Question,AttemptedQuestion
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.

last=[]
def home(request):
    context={}
    return render(request, 'courses/index.html',context)


def about(request):
    context={}
    return render(request, 'courses/about.html', context)


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

def course_summary(request, course_slug):
    courses = Courses.objects.get(slug=course_slug)
    context = {'courses':courses}
    return render(request, 'courses/course_summary.html', context)


def logout_view(request):
    logout(request)
    return redirect("/login")


def register(request):
    form = RegistrationForm(request.POST)     
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login')

    context = {'form': form}
    return render(request, 'courses/registration/sign_up.html', context=context)


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
    last.clear()
    return render(request,'quiz/dashboard.html')

@login_required
def play(request):
    quiz_profile, created = QuizProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        question_pk = request.POST.get('question_pk')

        attempted_question = quiz_profile.attempts.select_related('question').get(question__pk=question_pk)

        choice_pk = request.POST.get('choice_pk')

        try:
            selected_choice = attempted_question.question.choices.get(pk=choice_pk)
        except ObjectDoesNotExist:
            raise Http404

        quiz_profile.evaluate_attempt(attempted_question, selected_choice)

        return redirect(attempted_question)

    else:
        question = quiz_profile.get_new_question()
        if question is not None:
            quiz_profile.create_attempt(question)

        context = {
            'question': question,
        }

        return render(request, 'quiz/play.html', context=context)


@login_required
def submission_result(request, attempted_question_pk):
    attempted_question = get_object_or_404(AttemptedQuestion, pk=attempted_question_pk)
    context = {
        'attempted_question': attempted_question,
    }

    return render(request, 'quiz/submission_result.html')


def leaderboard(request):
    top_quiz_profiles = QuizProfile.get_rankings()[:500]
    total_count = top_quiz_profiles.count()
    context = {
        'top_quiz_profiles': top_quiz_profiles,
        'total_count': total_count,
    }
    return render(request, 'quiz/leaderboard.html', context=context)