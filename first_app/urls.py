from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('add/', views.addtask, name = 'addtask'),
    path('show/', views.showtasks, name = 'showtasks'),
    path('edit/<int:id>', views.edittask, name = 'edittask'),
    path('delete/<int:id>', views.deletetask, name = 'deletetask'),
    path('complete/<int:id>', views.completetask, name = 'completetask'),
    path('comp/', views.completion, name = 'complete'),
]