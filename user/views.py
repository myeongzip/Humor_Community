from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'user/index.html')


def show_poops(request):
    return render(request,'user/show_poops.html')


