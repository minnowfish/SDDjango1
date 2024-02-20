from django.shortcuts import render
from .models import Person

def splash(request):
    # username = request.POST["username"]
    name = 'Minnow'
    people = Person.objects.all()
    debug_people = list(people)
    return render(request, "splash.html", {'peoples':debug_people})