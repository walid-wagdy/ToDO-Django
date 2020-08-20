from django.urls import path
from . import views
from .views import PostListView, ToDoListCreateView, ToDoListUpdateView, ToDoListDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('todo/', views.todo, name='blog-todo'),
    path('todo/new/', ToDoListCreateView.as_view(), name='blog-new'),
    path('todo/update/<int:pk>', ToDoListUpdateView.as_view(), name='blog-update'),
    path('todo/delete/<int:pk>', ToDoListDeleteView.as_view(), name='blog-delete'),
]
