from django.urls import path

from users import views

urlpatterns = [
    path('groups/', views.GroupAPIView.as_view(), name='groups'),
    path('<str:username>/', views.UserAPIView.as_view(), name='user'),
    path('groups/<str:name>', views.AddGroupUsersAPIView.as_view(), name='users_to_group')
]