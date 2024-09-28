from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request): 
    restaurants = Restaurant.objects.all().order_by('name')
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    return render(request, 'restaurants/new.html')

def create(request):
    restaurant = Restaurant()
    restaurant.name = request.POST.get('name')
    restaurant.description = request.POST.get('description')
    restaurant.address = request.POST.get('address')
    restaurant.phone_number = request.POST.get('phone_number')
    restaurant.save()
    return redirect('restaurants:index')

def detail(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    context = {
        'restaurant' : restaurant
    }
    return render(request, 'restaurants/detail.html', context)

def edit(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    context = {
        'restaurant' : restaurant
    }
    return render(request, 'restaurants/edit.html', context)

def update(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    restaurant.name = request.POST.get('name')
    restaurant.description = request.POST.get('description')
    restaurant.address = request.POST.get('address')
    restaurant.phone_number = request.POST.get('phone_number')
    restaurant.save()
    return redirect('restaurants:index')

def delete(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    restaurant.delete()
    return redirect('restaurants:index')