import os
from datetime import datetime

from django.http import FileResponse
from django.shortcuts import render, redirect

from samplesite.settings import BASE_DIR
from testapp.forms import ImgForm

FILES_ROOT = BASE_DIR / 'files'


def index(request):
    imgs = []

    for entry in os.scandir(FILES_ROOT):
        imgs.append(os.path.basename(entry))
    context = {'imgs': imgs}
    return render(request, 'testapp/index.html', context)


def get(request, filename):
    fn = os.path.join(FILES_ROOT, filename)
    return FileResponse(open(fn, 'rb'), content_type='application/octet-stream')


def add(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file = request.FILES['img']
            fn = '%s%s' % (datetime.now().timestamp(),
                           os.path.splitext(upload_file.name)[1])
            fn = os.path.join(FILES_ROOT, fn)
            with open(fn, 'wb+') as destination:
                for chunk in upload_file.chunks():
                    destination.write(chunk)
            # return redirect('testapp:index')
            form.save()
            return redirect('testapp:index')
    else:
        form = ImgForm()

    context = {'form': form}
    return render(request, 'testapp/add.html', context)
