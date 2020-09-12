"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
# to import static files and media files
from django.conf import settings
from django.conf.urls.static import static
# model views
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # auth urls
    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),

    # basic urls
    path('', views.homepage, name='homepage'),
    path('404/', views.not_found, name='404'),

    # post urls
    path('posts/feed', views.post_list, name='feed'),
    path('posts/create', views.post_create, name='post_create'),
    path('posts/edit/<int:post_id>', views.post_edit, name='post_edit'),
    path('posts/delete/<int:post_id>', views.post_delete, name='post_delete'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)