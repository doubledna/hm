# Generated by Django 3.2.7 on 2021-09-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_alter_user_answer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='answer_time',
            field=models.CharField(default='1970-01-01 00:00:00', max_length=128, verbose_name='答题时间'),
        ),
    ]
