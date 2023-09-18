from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update, name='update'),
    # path('Tasks',views.Tasks,name='Tasks'),
    # path('add_task',views.add_task,name='add_task'),
]
