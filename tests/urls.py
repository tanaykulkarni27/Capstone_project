"""tests URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from main import views,__voice
urlpatterns = [
    path("vctotxt",__voice.home),
    path('RESTAPI',views.ACT.as_view()),
    path('logout',views.getout),
    path('login',views.LOG_IN),
    path('getin',views.GET_IN),
    path('Pupload',views.UPLOAD),
    path('upload',views.FILE_UPLOAD),
    path('', views.home),
    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)