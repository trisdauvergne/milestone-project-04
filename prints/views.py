from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import UploadPrintForm

from .models import Print
from django.contrib.auth.models import User

from profiles.models import DesignerProfile


def all_prints(request):
    """ A view to return all the prints on the site """
    all_prints = Print.objects.all()
    all_designers = DesignerProfile.objects.all()

    context = {
        'prints': all_prints,
        'designers': all_designers,
    }
    return render(request,
                  'prints/all_prints.html',
                  context)


def prints_by_designer(request):
    """ A view to return all the prints on the site """
    all_prints = Print.objects.all()
    all_designers = DesignerProfile.objects.all()
    all_designers_by_name = all_designers.order_by('last_name')

    context = {
        'prints': all_prints,
        'designers': all_designers_by_name,
    }
    return render(request,
                  'prints/all_prints_designer.html',
                  context)


def prints_by_price(request):
    """ A view to return all the prints on the site """
    all_prints = Print.objects.all()
    all_prints_by_price = all_prints.order_by('price')
    all_designers = DesignerProfile.objects.all()

    context = {
        'prints': all_prints_by_price,
        'designers': all_designers,
    }
    return render(request,
                  'prints/all_prints_price.html',
                  context)


def large_print(request, print_id):
    the_print = Print.objects.get(id=print_id)

    context = {
        'print': the_print,
    }

    return render(request,
                  'prints/large_print.html',
                  context)


@login_required
def add_print(request):
    """ A view to add a print to a page """
    designer = request.user

    upload_form = UploadPrintForm(instance=designer)

    if request.method == 'POST':
        upload_form = UploadPrintForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            return redirect('all_prints')
    else:
        upload_form = UploadPrintForm()
    return render(request,
                  'prints/add_print.html',
                  {'form': upload_form})


def edit_print(request, print_id):
    """ A view to edit a print """
    the_print = get_object_or_404(Print, id=print_id)
    if request.method == 'POST':
        form = UploadPrintForm(request.POST, request.FILES, instance=the_print)
        if form.is_valid():
            form.save()
            return redirect('all_prints')
    form = UploadPrintForm(instance=the_print)
    context = {
        'form': form,
    }
    return render(request,
                  'prints/edit_print.html',
                  context)


def delete_print(request, print_id):
    """ A view to delete a print """
    the_print = get_object_or_404(Print, id=print_id)
    the_print.delete()

    return redirect('all_prints')
