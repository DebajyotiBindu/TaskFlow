from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='landing'),
    path('task_list/',views.task_list,name='task_list'),
    path('add_task/',views.add_task,name='add_task'),
    path('task/<int:id>/edit_task/',views.edit_task,name='edit_task'),
    path('task/<int:id>/delete_task/',views.delete_task,name='delete_task'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]