from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessageListView.as_view()),
    path('<int:pk>/read/', views.mark_read),
    path('read_all/', views.mark_read_all)
]

app_name = 'inbox'
