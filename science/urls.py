from django.urls import path
from .views import ListTodo,DetailTodo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:pk>/',DetailTodo.as_view()),
    path('',ListTodo.as_view()),   
]
