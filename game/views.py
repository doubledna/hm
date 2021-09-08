import time
from django.shortcuts import render
from django import forms
from .models import User, Question


# Create your views here.
def index(request):
    """首页"""
    return render(request, 'game/index.html')


def test(request):
    """入群申请测试"""
    # questions = [
    #     {
    #         "question": "1 + 1 = ?",
    #         "answers": ["0", "1", "2", "3"]
    #     },
    #     {
    #         "question": "2 + 2 = ?",
    #         "answers": ["0", "2", "4", "6"]
    #     }
    # ]
    questions = []
    for question in Question.objects.all():
        question_dict = {"question": question.question, "answers": []}
        for option in question.questions_options.all():
            question_dict["answers"].append(option.options)
        questions.append(question_dict)
    # print(questions)
    return render(request, 'game/test.html', {"questions": questions})


def upload_answer(request):
    """上传答案，返回测试结果"""
    results = {}
    if request.method == "POST":
        resultss = request.POST
        # 获取玩家信息写入数据库
        name = resultss.get("name")
        qq = resultss.get("qq")
        # print(name, qq)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        us, _ = User.objects.update_or_create(qq=qq)  # 支持玩家二次更新分数
        # print(us)
        us.name = name
        us.answer_time = current_time
        us.save()
        # 获取玩家答题结果
        num = 0
        score = 0
        answer_record = ""
        for question in Question.objects.all():
            q = question.question
            player_answer = resultss.get(q, "空")
            # print(q, player_answer)
            qs = Question.objects.get(question=q)
            num = num + 1
            for op in qs.questions_options.all():
                if op.is_true:
                    if op.options == player_answer:
                        score = score + 10
                        answer_record = answer_record + "问题%s：%s ？、正确答案：%s、 你的回答：%s 得分：%s 分\n\n " % (num, q, op.options, player_answer, "10")
                    else:
                        answer_record = answer_record + "问题%s：%s ？、正确答案：%s、 你的回答：%s 得分：%s 分\n\n " % (num, q, op.options, player_answer, "0")
        us, _ = User.objects.update_or_create(qq=qq)
        us.score = score
        us.answer_record = answer_record
        us.save()
        # 结果返回给前端
        user = User.objects.filter(qq=qq)
        if user:
            us = User.objects.get(qq=qq)
            results = {"name": us.name,
                       "qq": qq,
                       "score": str(us.score),
                       "answer_time": us.answer_time,
                       "answer_record": us.answer_record}
        else:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            results = {"name": "-",
                       "qq": qq,
                       "score": "0",
                       "answer_time": current_time,
                       "answer_record": "你没有完成首页的 '入群申请' 或输入的QQ号有误，请回到首页重新入群申请或输入正确的QQ号！"}
    return render(request, 'game/upload_answer.html', {"results": results})


class ResultForm(forms.Form):
    qq = forms.CharField(label="QQ号")


def result(request):
    """返回申请人回答结果"""
    results = {}
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            qq = form.cleaned_data["qq"]
            # 查询用户
            user = User.objects.filter(qq=qq)
            if user:
                us = User.objects.get(qq=qq)
                results = {"name": us.name,
                           "qq": qq,
                           "score": str(us.score),
                           "answer_time": us.answer_time,
                           "answer_record": us.answer_record}
            else:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                results = {"name": "-",
                           "qq": qq,
                           "score": "0",
                           "answer_time": current_time,
                           "answer_record": "你没有完成首页的 '入群申请' 或输入的QQ号有误，请回到首页重新入群申请或输入正确的QQ号！"}

    else:
        form = ResultForm()
    return render(request, 'game/result.html', {"form": form, "results": results})

