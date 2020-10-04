from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from django.contrib.auth import views as login_views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token

from authentication import views

urlpatterns = [
    # path('', include('rest_framework.urls')),
    path('login/', obtain_auth_token),
    path('logout/', csrf_exempt(login_views.LogoutView.as_view())),
    path('token/', auth_views.obtain_auth_token, name='token'),
    path('register/', views.CreateUserAPIView.as_view(), name='register')
]
