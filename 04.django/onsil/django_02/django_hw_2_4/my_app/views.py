from django.shortcuts import render

# Create your views here.
def introduce(request, username):
    context = {
        'username': username,
    }
    return render(request, 'my_app/introduce.html', context)