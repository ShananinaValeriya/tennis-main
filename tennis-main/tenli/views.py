from django.shortcuts import render


def ligatennis(request):
    return render(request, "ligatennis.html")


def login(request):
    return render(request, "login.html")


def registration(request):
    return render(request, "registration.html")


def contact(request):
    return render(request, "contact.html")


def aboutus(request):
    return render(request, "aboutus.html")
