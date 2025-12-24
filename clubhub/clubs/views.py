from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Club ,Feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import FeedbackForm

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
    feedback_form = FeedbackForm()   # blank form by default

    if request.method == "POST":
        if "join" in request.POST:
            if request.user.clubs.count() >= 8:
                messages.error(request, "You can only join a maximum of 8 clubs.")
            else:
                club.members.add(request.user)
                messages.success(request, f"You joined {club.name}!")

        elif "request_leave" in request.POST:
            # Instead of removing, notify admin
            messages.info(request, "Your request to leave has been sent to the admin.")
            # Extend here: send email to admin or log request in DB

        elif "feedback" in request.POST:
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid():
                fb = feedback_form.save(commit=False)
                fb.club = club
                fb.user = request.user
                fb.save()
                messages.success(request, "Your feedback has been submitted!")

        return redirect("club_detail", club_id=club.id)

    return render(
        request,
        "club_detail.html",
        {
            "club": club,
            "feedback_form": feedback_form,
        },
    )


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
