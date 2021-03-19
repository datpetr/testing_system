from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'office_teacher/office_teacher.html')


def making_test(request):
    return render(request, 'making_test/making_test.html')
