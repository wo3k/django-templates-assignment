from django.shortcuts import render

from datetime import date

def home(request):
    context = {
        "first_name": "belal",
        "last_name": " Jnena",
        "student_id": "120221646",
        "address": "Palestine - Gaza",
        "email": "belaljenana2@gmail.com",
        "note": "This page is for my Templates assignment",
        "dob": date(2004, 5, 13),
    }
    return render(request, "pages/index.html", context)
