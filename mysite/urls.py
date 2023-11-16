"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('userclient/', views.userclient, name='userclient'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('about/', views.about, name='about'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('editProfile/', views.edit_profile, name='editProfile'),
    path('search/', views.search, name='search'),
    path('avance_search/', views.avance_search, name='avance_search'),
     path('photographer/<int:pk>/', views.photographer_detail, name='photographer_detail'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)