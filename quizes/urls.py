"""goli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from quizes import views

urlpatterns = [
    path('<int:pk>/', views.QuizAPIView.as_view()),
    path('', views.QuizListAPIView.as_view()),
    path('create/', views.CreateQuizAPIView.as_view()),
    path('<int:pk>/vote/', views.VoteAPIView.as_view()),
    path('<int:pk>/votes/', views.ListVoteAPIView.as_view()),
    path('<int:pk>/votes/count/', views.ListCountVoteAPIView.as_view()),
]
