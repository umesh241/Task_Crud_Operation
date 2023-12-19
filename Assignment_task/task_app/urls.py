from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup),
    path('add/', views.add_Task),
    path('delete/<int:id>', views.delete_Task),
    path('edit/<int:id>/<str:status>', views.change_Task),
    path('logout/', views.signout),
    path('Task-list/', views.listTask, name='Task-list'),
    path('list-detail/<str:pk>/', views.listTaskDetail, name='list-detail'),
    path('Task_delete/<str:pk>/', views.Task_delete, name='Task_delete'),
]
