from django.urls import path

from testapp.views import add, index, get

app_name = 'testapp'

urlpatterns = [
    path('add/', add, name='add'),
    path('get/<path:filename>/', get, name='get'),
    path('', index, name='index'),
]
