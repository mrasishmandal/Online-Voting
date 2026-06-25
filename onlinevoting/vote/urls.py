from django.urls import path
from . import views

# URL routing configuration specific to the vote application
urlpatterns = [    
    path('', views.home, name='home'),                      # Home page route
    path('register/', views.register, name='register'),      # Registration page route
    path('vote/', views.vote, name='vote'),                  # Voting page route
    path('results/', views.results, name='results'),          # Results page route
]