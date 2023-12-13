from django.shortcuts import render
from .signup import Forms

def home(request):
  return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = Forms(request.POST)
        if form.is_valid():
            pass
    else:
        form = Forms()

    return render(request, 'signup.html', {'form': form})

def start(request):
    return render(request, 'start.html')