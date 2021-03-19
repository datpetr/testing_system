from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'teacher_name': 'Имя Фамилия',
        'tests': [{'title': 'Матан', 'class': '10'}, {'title': 'Русич', 'class': '9'}]
    }
    return render(request, 'office_teacher/office_teacher.html', data)


def making_test(request):
    data = {
        'questions': [{'title': 'Как?'}, {'title': 'Где?'}, {'title': 'Когда?'}]
    }
    return render(request, 'making_test/making_test.html', data)
