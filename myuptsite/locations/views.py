from django.shortcuts import render, get_object_or_404, redirect
from .forms import LocationForm
from .models import Location

# Create your views here.


# def location_view(request, *args, **kwargs):
#     #obj = get_object_or_404(Location, id=id)
#     my_context = {
#         "description": "This is a description!"
#     }
#     return render(request, "locations/location_main.html", my_context)




def location_create_view(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LocationForm()
    context = {
        'form': form
    }
    return render(request, "locations/location_create.html", context)


def location_update_view(request, id=id):
    obj = get_object_or_404(Location, id=id)
    form = LocationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "locations/location_create.html", context)


def location_list_view(request):
    queryset = Location.objects.all() # list of objects
    context = {
        "object_list": queryset
        }
    print(context)
    return render(request, "locations/location_list.html", context)


def location_detail_view(request, id):
    obj = get_object_or_404(Location, id=id)
    context = {
        "object": obj
    }
    return render(request, "locations/location_detail.html", context)


def location_delete_view(request, id):
    obj = get_object_or_404(Location, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "locations/location_delete.html", context)