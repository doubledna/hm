# coding=utf8
"""路由"""
from django.urls import path
from .views import index

# create code to here
urlpatterns = [
    path("index", index, name="index"),
]
