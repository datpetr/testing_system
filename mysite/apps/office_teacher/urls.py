from django.urls import path
from . import views

app_name = 'office_teacher'

urlpatterns = [
    # path('making_test/', views.making_test, name='making_test'),
    path('making_test', views.making_test, name='making_test'),
    path('', views.index, name='index')
]
