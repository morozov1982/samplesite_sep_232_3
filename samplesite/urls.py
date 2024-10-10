"""
URL configuration for samplesite project.

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
from tempfile import template

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/login/', LoginView.as_view(), name='login'),
    # path('accounts/logout/',
    #      LogoutView.as_view(next_page='bboard:index'), name='logout'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path('accounts/password_change/',
         PasswordChangeView.as_view(
             template_name='registration/change_password.html'),
         name='password_change'),
    path('accounts/password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='registration/password_changed.html'),
         name='password_change_done'),

    path('testapp/', include('testapp.urls', namespace='testapp')),
    path('', include('bboard.urls', namespace='bboard')),
]

urlpatterns += [
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.THUMBNAIL_MEDIA_URL,
#                       document_root=settings.THUMBNAIL_MEDIA_ROOT)
