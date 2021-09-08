from django.contrib import admin
from .models import User, Question, Options, Answer


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    玩家
    """
    list_display = ("name", "qq", "score",)
    list_per_page = 50
    list_filter = ("name", "qq", "score",)
    search_fields = ("name", "qq",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    问题
    """
    list_display = ("question",)
    list_per_page = 50
    list_filter = ("question",)
    search_fields = ("question",)


@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    """
    选项
    """
    list_display = ("question", "options", "is_true",)
    list_per_page = 50
    list_filter = ("question", "options",)
    search_fields = ("question__question", "options",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
    玩家回答结果
    """
    list_display = ("user", "question", "answer", "is_true")
    list_per_page = 50
    list_filter = ("user",)
    search_fields = ("user__name",)
