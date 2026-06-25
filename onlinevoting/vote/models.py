from django.db import models
from django.contrib.auth.models import User

# Model representing a candidate in the election 
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

# Model representing a user's single vote 
class Vote(models.Model):
    user = models.OneToOneField( # Ensures one user can vote only once 
        User,
        on_delete=models.CASCADE
    )
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name}"