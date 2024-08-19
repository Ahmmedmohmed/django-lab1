from django.urls import path
from . import views

app_name = 'trainee'

urlpatterns = [
    path('', views.list_trainee, name='list'),
    path('create/', views.create_trainee, name='create'),
    path('<int:pk>/', views.trainee_detail, name='detail'),
    path('<int:pk>/update/', views.update_trainee, name='update'),
    path('<int:pk>/delete/', views.delete_trainee, name='delete'),
]
