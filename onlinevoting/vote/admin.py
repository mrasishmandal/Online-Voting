from django.contrib import admin
from .models import Candidate, Vote

# Register Candidate model to manage candidates in admin panel
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'party']

# Register Vote model to monitor cast votes in admin panel
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'candidate', 'timestamp']