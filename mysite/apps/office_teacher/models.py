from django.db import models


class Test(models.Model):
    test_title = models.CharField('название теста', max_length=200)
    test_text = models.IntegerField('количество вопросов')


class Question(models.Model):
    question_title = models.TextField('введите вопрос ответа')
    first_var = models.TextField('введите первый вариант ответа')
    second_var = models.TextField('введите второй вариант ответа')
    third_var = models.TextField('введите третий вариант ответа')
    fourth_var = models.TextField('введите четвёртый вариант ответа')
