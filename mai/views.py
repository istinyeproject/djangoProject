from django.shortcuts import render

from .models import Publication, Person


def main(request):
    publications = [c for c in Publication.objects.all()]
    people = [c for c in Person.objects.all()]

    return render(request, 'mai/index.html', {"publications":publications, "people":people})


