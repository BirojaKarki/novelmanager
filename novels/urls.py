
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_novel, name='add_novel'),
    path('update/<int:id>/', views.update_novel, name='update_novel'),
    path('delete/<int:id>/', views.delete_novel, name='delete_novel'),
]
