from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Club

def homepage(request):
    return render(request, "homepage.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def club_list(request):
    clubs = Club.objects.all()
    return render(request, "club_list.html", {"clubs": clubs})

def club_detail(request, club_id):
    club = Club.objects.get(id=club_id)
    return render(request, "club_detail.html", {"club": club})
