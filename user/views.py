from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'user/index.html')


def feed_view(request):
    return render(request,'user/feed.html')


