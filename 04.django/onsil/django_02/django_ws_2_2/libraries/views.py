from django.shortcuts import render

# Create your views here.
def intro(request):
    return render(request, 'libraries/intro.html')