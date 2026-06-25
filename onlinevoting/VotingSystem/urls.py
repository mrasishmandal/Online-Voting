from django.contrib import admin
from django.urls import path, include

# Global URL configuration for VotingSystem project
urlpatterns = [   
    path('admin/', admin.site.urls),                   # Route for the Django admin panel 
    path('', include('vote.urls')),                    # Route for the voting app functionalities 
    path('accounts/', include('django.contrib.auth.urls')), # Built-in authentication URLs (login/logout) 
]