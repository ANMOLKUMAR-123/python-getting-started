from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "landscape/about.html")


def home(request):
    return render(request, "home.html")


def result(request):
    return render(request, "result.html")


def service(request):
    return render(request, "service.html")


