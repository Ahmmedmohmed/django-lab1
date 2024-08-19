from django.urls import path
from . import views

app_name = 'track'

urlpatterns = [
    path('', views.list_track, name='list'),
    path('create/', views.create_track, name='create'),
    path('<int:pk>/', views.track_detail, name='detail'),
    path('<int:pk>/update/', views.update_track, name='update'),
    path('<int:pk>/delete/', views.delete_track, name='delete'),
]
