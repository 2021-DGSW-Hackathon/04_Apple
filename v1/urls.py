from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from . import views

app_name = 'v1'
urlpatterns = [
    path('programInfo/', views.programInfo.as_view(), name='index'),
    path('signUp/', views.signUp.as_view(), name='index'),
    path('login/', views.logIn.as_view(), name='index'),
    path('checkToken/', views.checkToken.as_view(), name='index'),
    path('programs/', views.programs.as_view(), name='index'),
    path('programs_make/', views.programs_make.as_view(), name='index'),
    path('programs_delete/', views.programs_delete.as_view(), name='index'),
    path('programs_modify/', views.programs_modify.as_view(), name='index'),
]