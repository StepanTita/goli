from django.urls import path

from users import views

urlpatterns = [
    path('groups/', views.CreateGroupAPIView.as_view(), name='groups'),
    path('<int:user>/', views.GetUserAPIView.as_view(), name='user'),
    path('groups/<str:group>', views.AddGroupUsersAPIView.as_view(), name='users_to_group')
]