# Generated by Django 3.2.7 on 2021-09-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_alter_user_answer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='answer_time',
            field=models.CharField(default='2021-09-08 15:10:25', max_length=128, verbose_name='答题时间'),
        ),
    ]
