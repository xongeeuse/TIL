from django.shortcuts import redirect, render, get_object_or_404
from .models import Travel
from .forms import TravelForm
from django.views.decorators.http import require_http_methods, require_safe, require_POST

# Create your views here.

@require_safe
def index(request):
    travels = Travel.objects.all()
    context = {
        'travels':travels
    }
    return render(request,'travels/index.html',context)

@require_http_methods(["GET","POST"])
def create(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid:
            travel = form.save()
            return redirect('travels:detail',travel.pk)
    else:
        form = TravelForm()
    context={
        'form':form
    }
    return render(request,'travels/create.html',context)

@require_safe
def detail(request,pk):
    travel = get_object_or_404(Travel,pk=pk)
    context = {
        'travel':travel
    }
    return render(request,'travels/detail.html',context)

# @require_http_methods(["POST"])
@require_POST
def delete(request, pk):
    travel = get_object_or_404(Travel,pk=pk)
    # travel = Travel.objects.get(pk=pk)
    travel.delete()
    return redirect('travels:index')

@require_http_methods(["GET", "POST"])
def update(request, pk):
    travel = Travel.objects.get(pk=pk)
    if request.method == 'POST':
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = TravelForm(instance=travel)
    context = {
        'travel' : travel,
        'form' : form,
    }
    return render(request, 'travels/update.html', context)


