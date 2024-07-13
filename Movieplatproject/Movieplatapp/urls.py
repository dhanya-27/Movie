from django.urls import path
from Movieplatapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('',views.add_movie,name='add_movie'),
    path('signUp/', views.signUp, name='signUp'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('watch/', views.watch, name='watch'),
    path('recommend/', views.recommend, name='recommend'),
]