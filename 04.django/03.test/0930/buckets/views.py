from django.shortcuts import render, redirect
from .models import TravelBucketList
from .forms import TravelBucketListForm


# Create your views here.

def index(request):
    travel_bucket_lists = TravelBucketList.objects.all()
    context = {
        'travel_bucket_lists': travel_bucket_lists
    }
    return render(request, 'buckets/index.html', context)


def about(request):
    return render(request, 'buckets/about.html')


def detail(request, bucket_pk):
    bucket_item = TravelBucketList.objects.get(pk=bucket_pk)
    context = {
        'bucket_item': bucket_item
    }
    return render(request, 'buckets/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = TravelBucketListForm(request.POST, request.FILES)
        if form.is_valid():
            travel_bucket_list_item = form.save()
            return redirect('buckets:detail', travel_bucket_list_item.pk)
    else:
        form = TravelBucketListForm()
    context = {
        'form': form
    }
    return render(request, 'buckets/create.html', context)


def update(request, bucket_pk):
    bucket_item = TravelBucketList.objects.get(pk=bucket_pk)
    if request.method == 'POST':
        form = TravelBucketListForm(request.POST, request.FILES, instance=bucket_item)
        if form.is_valid():
            travel_bucket_list_item = form.save()
            return redirect('buckets:detail', travel_bucket_list_item.pk)
    else:
        form = TravelBucketListForm(instance=bucket_item)
    context = {
        'bucket_item': bucket_item,
        'form': form
    }
    return render(request, 'buckets/update.html', context)


def delete(request, bucket_pk):
    bucket_item = TravelBucketList.objects.get(pk=bucket_pk)
    if request.method == 'POST':
        bucket_item.delete()
        return redirect('buckets:index')

    return redirect('buckets:detail', bucket_pk)
