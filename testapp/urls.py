from django.urls import path

from testapp.views import add

app_name = 'testapp'

urlpatterns = [
    path('add/', add, name='add'),
    # path('', index, name='index'),
]
