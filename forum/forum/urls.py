"""
URL configuration for forum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path, include
from forum_IT.views import home_view, create_post, view_posts, register, terms_view, delete_post

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('create_post/', create_post, name='create_post'),
    path('view_posts/', view_posts, name='view_posts'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('terms/', terms_view, name='terms'),
    path('post/delete/<int:post_id>/', delete_post, name='delete_post'),
]
