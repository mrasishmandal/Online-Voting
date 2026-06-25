from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, VoteForm
from .models import Candidate, Vote

# Renders the main entrance or welcome page of the system
def home(request):
    return render(request, 'vote/home.html')

# Handles new user registrations and logs them in automatically
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Authenticates and logs in the newly registered user
            return redirect('vote') # Redirects to the voting panel
    else:  
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# Handles casting a vote and prevents double voting
@login_required
def vote(request):
    if Vote.objects.filter(user=request.user).exists():
        messages.warning(request, "You have already voted.")
        return redirect('results')
        
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user
            vote.save()
            return redirect('results')
    else:
        form = VoteForm()
    return render(request, 'vote/vote.html', {'form': form})

# Computes and displays the aggregated voting results for each candidate
@login_required
def results(request):
    candidates = Candidate.objects.all()
    vote_count = {
        candidate: Vote.objects.filter(candidate=candidate).count()
        for candidate in candidates
    }
    return render(request, 'vote/results.html', {'vote_count': vote_count})