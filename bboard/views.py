from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from bboard.models import Bb


# def index(request):
#     template = loader.get_template('bboard/index.html')
#     bbs = Bb.objects.order_by('-published')
#     context = {'bbs': bbs}
#
#     return HttpResponse(template.render(context, request))


def index(request):
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}

    return render(request, 'bboard/index.html', context)
