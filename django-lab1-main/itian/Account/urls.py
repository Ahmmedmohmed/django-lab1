from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.list_accounts, name='list'),
    path('create/', views.create_account, name='create'),
    path('<int:pk>/', views.account_detail, name='detail'),
    path('<int:pk>/update/', views.update_account, name='update'),
    path('<int:pk>/delete/', views.delete_account, name='delete'),
]
