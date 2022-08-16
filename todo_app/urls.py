from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('edit',views.edit,name='edit'),
    path('log',views.log,name='log'),
    path('profile',views.profile,name='profile'),
    path('sign',views.sign,name='sign'),
    path('add_task',views.add_task,name='add_task'),
    path('delete',views.delete,name='delete'),
    path('edit_task',views.edit_task,name='edit_task'),
]

