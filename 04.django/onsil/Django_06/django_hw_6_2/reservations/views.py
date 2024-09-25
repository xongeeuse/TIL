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

def new(request):
    form = ReservationForm()
    context = {
        'form' : form,
    }
    return render(request, 'reservations/new.html', context)

def create(request):
    # 모델폼 인스턴스 생성
    form = ReservationForm(request.POST)
    # 유효성 검사
    # 통과하면 저장하고 인덱스 페이지로 리다이렉트
    if form.is_valid():
        reservation = form.save()
        return redirect('reservations:index')
    # 통과하지 못했다면 에러메세지와 함께 new페이지 다시 렌더
    context = {
        'form' : form,
    }
    return render(request, 'reservations/new.html', context)