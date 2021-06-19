from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('classes/', views.classes, name="classes"),
    path('dash/', views.dash, name="dash"),
    path('grades/', views.grades, name="grades"),
    # path('login/', views.loginPage, name="login"),
    path('signup/', views.registerPage, name="signup"),
    path('students/', views.showStudents, name="students"),
]
