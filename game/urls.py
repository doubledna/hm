# coding=utf8
"""路由"""
from django.urls import path
from .views import index, test, result, upload_answer

# create code to here
urlpatterns = [
    # path("index", index, name="index"),
    # path("rules/", rules, name="rules"),
    # path("staff", staff, name="staff"),
    # path("vote", vote, name="vote"),
    # path("test/", test, name="index"),
    path("upload_answer/", upload_answer, name="upload_answer"),
    path("result/", result, name="result"),
]
