from django.urls import path, re_path

from bboard.models import Bb
from bboard.views import (index, by_rubric, BbCreateView, add_and_save, detail,
                         BbByRubricView)  # add, add_save

app_name = 'bboard'

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    # path('add/', BbCreateView.as_view(model=Bb,
    #                                   template_name='bboard/create.html'), name='add'),
    # path('add/save/', add_save, name='add_save'),
    # path('add/', add, name='add'),
    # path('add/', add_and_save, name='add'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('detail/<int:bb_id>/', detail, name='detail'),
    path('', index, name='index'),
]
