from django.http import HttpResponse
from django.shortcuts import redirect, render

from tweet.models import Tweet

# Create your views here.

def index(request):
    if request.method == "GET":
        tweets = Tweet.objects.all()
        print(tweets)
        context = {
            "tweets":tweets,   
        }
        return render(request, "user/feed.html", context)
    else:
        return HttpResponse("Invalid request method", status=405)

def todo_create(request):
    if request.method == "POST":
        Tweet.objects.create(
            content=request.POST['content'], 
            user=request.user,
            image = request.FILES.get("image")
        )
        return redirect("/feed/")
    elif request.method == "GET":
        return render(request, "tweet/create.html")
    else:
        return HttpResponse("Invalid request method", status=405)
