from django.contrib import admin
from django.urls import path, include
from log import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('log/new/', views.create_log, name='create_log'),
    path('idea/new/', views.create_idea, name='create_idea'),
    path('post/new/', views.create_post, name='create_post'),
    path('log/<int:pk>/edit/', views.edit_log, name='edit_log'),
    path('idea/<int:pk>/edit/', views.edit_idea, name='edit_idea'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('log/<int:pk>/delete/', views.delete_log, name='delete_log'),
    path('idea/<int:pk>/delete/', views.delete_idea, name='delete_idea'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
]
