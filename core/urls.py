
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('signup/', views.signup_page, name='signup'),
    path('add-project/', views.add_project, name='add_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
path('project/<int:project_id>/add-task/', views.add_task, name='add_task'),
path('task/<int:task_id>/update/', views.update_task_status, name='update_task'),
path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
path('project/<int:project_id>/edit/', views.edit_project, name='edit_project'),
path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
]


