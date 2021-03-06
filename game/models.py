from django.db import models


# Create your models here.
# 用户
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name="名字")
    qq = models.CharField(unique=True, max_length=128, verbose_name="QQ号")
    score = models.IntegerField(verbose_name="答题分数", default=0)
    answer_time = models.CharField(max_length=128, verbose_name="答题时间", default="1970-01-01 00:00:00")
    answer_record = models.TextField(verbose_name="答题记录", default="-")

    def __str__(self):
        return '%s' % (self.qq,)

    class Meta:
        verbose_name = "玩家"
        verbose_name_plural = "玩家"


# 问题
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(unique=True, max_length=1024, verbose_name="问题")

    def __str__(self):
        return '%s' % (self.question,)

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = "问题"


# 问题的选项
class Options(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, verbose_name="问题", on_delete=models.CASCADE, related_name="questions_options")
    options = models.CharField(max_length=1024, verbose_name="选项")
    is_true = models.BooleanField(verbose_name="正确还是错误选项")

    def __str__(self):
        return '%s' % (self.options,)

    class Meta:
        verbose_name = "问题选项"
        verbose_name_plural = "问题选项"


# 用户回答问题结果
class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name="玩家", on_delete=models.CASCADE, related_name="answer_user")
    question = models.ForeignKey(Question, verbose_name="问题", related_name="answer_questions", on_delete=models.CASCADE)
    answer = models.ForeignKey(Options, verbose_name="选择答案", related_name="answer_options", on_delete=models.CASCADE)
    is_true = models.BooleanField(verbose_name="回答是否正确", default=False)

    def __str__(self):
        return '%s' % (self.id,)

    class Meta:
        verbose_name = "玩家回答结果"
        verbose_name_plural = "玩家回答结果"
