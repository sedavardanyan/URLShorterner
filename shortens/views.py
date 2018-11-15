from django.shortcuts import render, redirect
from .models import Url
from django.contrib.auth.decorators import login_required
import random
import string


@login_required
def create(request):
    if request.method == "POST":
        url = Url()
        url.original = request.POST['link']
        url.author = request.user
        url.shortened = f"http://{request.get_host()}/{shorten()}"
        url.save()
        return render(request, 'shortens/create.html', {"link": url.shortened})
    else:
        return render(request, 'shortens/create.html')


def check(request):
    if request.method == "POST":
        url = Url.objects.get(shortened=request.POST['link'])
        return render(request, 'shortens/check.html', {"link": url.visits})
    else:
        return render(request, 'shortens/check.html')


def home(request):
    return render(request, 'shortens/home.html')


def shorten()-> str:
    print(hash(url))
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(5))


def shortened(request):
    url = Url.objects.get(shortened=f"http://{request.get_host()}{request.path}")
    url.visits += 1
    url.save()
    return redirect(url.original)


