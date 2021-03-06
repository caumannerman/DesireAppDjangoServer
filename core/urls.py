"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include

urlpatterns = [
    # Django admin site
    path('admin/', admin.site.urls),

    # REST Framework
    path('api-auth/', include('rest_framework.urls')),

    # API
    path('api/v1/auth/', include('auth.urls')),
    path('api/v1/users/', include('accounts.urls')),

    path('api/v1/questions/', include('questions.urls')),
    path('api/v1/answers/', include('answers.urls')),
    path('api/v1/answer-evaluations/', include('answer_evaluations.urls')),
    path('api/v1/chat-rooms/', include('chatrooms.urls')),
    path('api/v1/chat-messages/', include('chatmessages.urls')),
    path('api/v1/uploaded-audios/', include('uploads.audios.urls')),
    path('api/v1/uploaded-images/', include('uploads.images.urls')),
    path('api/v1/uploaded-files/', include('uploads.files.urls')),
    path('api/v1/uploaded-videos/', include('uploads.videos.urls')),

    # # django-rest-auth
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
