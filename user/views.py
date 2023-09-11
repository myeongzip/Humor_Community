from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'user/index.html')


def show_home(request):
    return render(request,'user/home.html')

def signup(request):
    return render(request, 'account/signup.html')
