from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


app_name='courses'

urlpatterns = [
    # path('',views.home, name='home'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about_us'),
    path('registration/',views.register, name='registration'),
    path('login/', views.login_view, name='login'),
    path('dashboard/',views.dashboard , name='dashboard'),
    path('logout/',views.logout_view, name='logout'),   
    path('courses/', views.courses_list, name='course_list' ),
    path('category/<slug:category_slug>/', views.courses_list, name='category_list_by_category'),
 
    path('courses/<slug:course_slug>/',views.course_summary, name = 'course_summary'),
    
    # reset password
    
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='courses/registration/password_reset.html'),
         name='reset_password')
    ,
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='courses/registration/password_reset_sent.html'),
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='courses/registration/password_reset_form.html'),
         name='password_reset_confirm'),
    
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='courses/registration/password_reset_done.html'),
         name='password_reset_complete'), 

     path('leaderboard/', views.leaderboard, name='leaderboard'),
     
     url(r'^submission-result/(?P<attempted_question_pk>\d+)/', views.submission_result, name='submission_result'),
     
     
     path('play/',views.play, name='play'),

]
