"""
URL configuration for GrabNGo_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import *
from Base_App import views

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name="Home"),
    path('book_table',BookTableView,name="Book_Table"),
    path('menu',MenuView,name="Menu"),
    path('about',AboutView,name="About"),
    path('feedback',FeedbackView,name="Feedback_Form"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('book_table_redirect/', views.book_table_redirect, name='book_table_redirect'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

