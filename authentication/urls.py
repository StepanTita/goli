from django.urls import path, include
from rest_framework.authtoken import views as auth_views

from authentication import views

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('token/', auth_views.obtain_auth_token, name='token'),
    path('register/', views.CreateUserAPIView.as_view(), name='register')
]
