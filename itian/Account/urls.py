from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.list_accounts, name='list'),
    path('create/', creat, name='create'),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/update/', update, name='update'),
    path('<int:pk>/delete/', delet, name='delete'),
]
