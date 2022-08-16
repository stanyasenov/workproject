from django.shortcuts import render

from workproject.work.models import Module


def modules_data(request):
    filtered_modules = Module.objects.filter(user_id=1000)

    return render(request, 'index.html', {'posts':  filtered_modules})


