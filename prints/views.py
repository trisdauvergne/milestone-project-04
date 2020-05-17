from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UploadPrintForm

from .models import Print
from profiles.models import RegisteredUserProfile


def all_prints(request):
    """ A view to return all the prints on the site """
    all_prints = Print.objects.all()
    all_designers = RegisteredUserProfile.objects.all()

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
    ordered_prints = all_prints.order_by('designer')
    print(ordered_prints)
    all_designers = RegisteredUserProfile.objects.all()
    # print(all_designers)
    all_designers_by_name = all_designers.order_by('last_name')
    print(all_designers_by_name)

    context = {
        'prints': ordered_prints,
        'designers': all_designers_by_name,
    }
    return render(request,
                  'prints/all_prints_designer.html',
                  context)


def prints_by_price(request):
    """ A view to return all the prints on the site """
    all_prints = Print.objects.all()
    all_prints_by_price = all_prints.order_by('price')
    all_designers = RegisteredUserProfile.objects.all()

    context = {
        'prints': all_prints_by_price,
        'designers': all_designers,
    }
    return render(request,
                  'prints/all_prints_price.html',
                  context)


def large_print(request, print_id):
    """ A view to see individual prints and for designers to edit their uploads """
    # # Get the logged in user's ID
    user = request.user
    designer_id = None
    if user.is_authenticated:
        designer = get_object_or_404(RegisteredUserProfile, user=user)
        designer_id = designer.id
    # print(designer_id)

    # Calling the print from the database
    the_print = Print.objects.get(id=print_id)

    context = {
        'print': the_print,
        'designer_id': designer_id,
    }

    return render(request,
                  'prints/large_print.html',
                  context)


@login_required
def add_print(request):
    """ A view to add a print to a page """
    user = request.user

    designer = get_object_or_404(RegisteredUserProfile,
                                 user=user)

    upload_form = UploadPrintForm()  # some random comment

    if request.method == 'POST':
        upload_form = UploadPrintForm(request.POST,
                                      request.FILES)

    # Remove print statements

        if upload_form.is_valid():
            print("*********")
            print(type(upload_form))
            upload_form = upload_form.save(commit=False)
            print("*********")
            print(type(upload_form))
            upload_form.designer = designer
            upload_form.save()
            messages.success(request, f'Your print was uploaded!')
            return redirect('all_prints')
    else:
        upload_form = UploadPrintForm()
    return render(request,
                  'prints/add_print.html',
                  {'form': upload_form})


@login_required
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


@login_required
def delete_print(request, print_id):
    """ A view to delete a print """
    the_print = get_object_or_404(Print, id=print_id)
    the_print.delete()

    return redirect('all_prints')
