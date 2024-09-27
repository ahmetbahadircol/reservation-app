from django.shortcuts import render


def homepage(request):
    return render(request, "accounts/templates/accounts/base.html")
