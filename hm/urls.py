"""hm URL Configuration

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
from django.conf.urls import include
from game.views import index, rules, staff, vote, message_wall, download, join


urlpatterns = [
    path("", index, name="index"),
    path("index/", index, name="index"),
    path("rules/", rules, name="rules"),
    path("staff/", staff, name="staff"),
    path("vote/", vote, name="vote"),
    path("message_wall/", message_wall, name="message_wall"),
    path("download/", download, name="download"),
    path("join/", join, name="join"),
    path('admin/', admin.site.urls),
    path('game/', include('game.urls'), name="game"),
    # url(r'^favicon\.ico$',RedirectView.as_view(url=r'static/img/favicon.ico')),
]
