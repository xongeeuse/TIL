from django.shortcuts import render
from .models import Garage

# Create your views here.
def index(request):
    
    context = {
        'in_dokdo' : Garage.objects.filter(location='독도'),
        'under_thirty' : Garage.objects.filter(capacity__lte=30),
        'availables' : Garage.objects.filter(is_parking_available=1)
    }
    return render(request, 'garages/index.html', context)