from django.shortcuts import render

from django.shortcuts import render

def home(request):
    context = {
        "full_name": "Belal Jnena",
        "student_id": "120221646",
        "address": "Palestine - Gaza",
        "email": "belaljenana2@gmail.com",
        "note": "This page is for my Templates assignment",
    }
    return render(request, "pages/index.html", context)
