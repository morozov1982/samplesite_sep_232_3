import os.path
from datetime import datetime

from django.shortcuts import render, redirect

from samplesite.settings import BASE_DIR
from testapp.forms import ImgForm

FILES_ROOT = BASE_DIR / 'files'

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
            return redirect('bboard:index')
    else:
        form = ImgForm()

    context = {'form': form}
    return render(request, 'testapp/add.html', context)
