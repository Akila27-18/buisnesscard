# profile/views.py
from django.shortcuts import render

def card_view(request):
    context = {
        "name": "Akila Barathkumar",
        "title": "Fullstack Engineer",
        "email": "akila271819@gmail.com",
        "phone": "+91-9876543210",
        "linkedin": "https://www.linkedin.com/Akilak7",
        "image": "images/profile.png"
    }
    
    
    return render(request, "card.html", context)