from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import FileView, FileViewDetail

urlpatterns = [
    path('', views.taskList, name='tasks'),
    #path('users/', views.UserList.as_view()),
    #path('users/<int:pk>/', views.UserDetail.as_view()),
    path('todo/', views.ToDoList.as_view()),
    path('todo/<int:pk>/', views.ToDoDetail.as_view()),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('files/', FileView.as_view(), name='file-upload'),
    path('files/<str:pk>', FileViewDetail.as_view(), name='file-download'),
]
