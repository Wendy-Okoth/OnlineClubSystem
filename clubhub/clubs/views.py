from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Club
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

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

@login_required 
def club_detail(request, club_id): 
    club = get_object_or_404(Club, id=club_id) 
    # Handle join/leave actions 
    if request.method == "POST": 
        if "join" in request.POST: # enforce max 8 clubs per user 
            if request.user.clubs.count() >= 8: 
                messages.error(request, "You can only join a maximum of 8 clubs.") 
            else:
                club.members.add(request.user) 
                messages.success(request, f"You joined {club.name}!") 
        elif "leave" in request.POST: 
            club.members.remove(request.user)
            messages.info(request, f"You left {club.name}.")
        return redirect("club_detail", club_id=club.id) 
    return render(request, "club_detail.html", {"club": club})

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def recent_clubs(request):
    clubs = request.user.clubs.all()  # thanks to the ManyToManyField
    return render(request, "recent_clubs.html", {"clubs": clubs})

def logout_view(request): 
    logout(request) # this clears the session and logs the user out 
    return redirect("homepage")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def events(request):
    return render(request, "events.html")

@login_required
def reviews(request):
    # later you can query Review objects
    return render(request, "reviews.html")
