from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

# def new(request):
#     form = ReservationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'reservations/new.html', context)

# def create(request):
#     form = ReservationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('reservations:index')
#     context = {
#         'form': form
#     }
#     return render(request, 'reservations/new.html', context)

def create(request):
    # 요청이 POST로 들어온다면
    if request.method == 'POST':
        # 기존 create 함수 기능 수행
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations:index')
    # 요청이 POST가 아니라면
    else:
        # 기존 new 함수의 기능 수행
        form = ReservationForm()
    context = {
        'form' : form,
    }
    return render(request, 'reservations/create.html', context)
        
    
