from django.shortcuts import render, redirect

from .forms import UploadPrintForm

from .models import Print


def all_prints(request):
    """ A view to return all the prints on the site """
    all_prints = Print.objects.all()

    context = {
        'prints': all_prints,
    }
    return render(request,
                  'prints/all_prints.html',
                  context)


def add_print(request):
    """ A view to add a print to a page """
    form = UploadPrintForm()
    if request.method == 'POST':
        form = UploadPrintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_prints')
    else:
        form = UploadPrintForm()
    return render(request,
                  'prints/add_print.html',
                  {'form': form})

