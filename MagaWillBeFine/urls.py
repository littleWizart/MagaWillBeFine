from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from Diplom import views
from Diplom.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include('django.contrib.auth.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('base', views.base),
    path('events1', EventView.as_view(), name = 'posts'),
    path('events/', AddEventView.as_view(), name = 'add_event'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)