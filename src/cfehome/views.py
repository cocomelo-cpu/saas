from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home(request):
    queryset = PageVisit.objects.all().count()
    title = "My page"
    PageVisit.objects.create()
    context = {
        'title': title,
        'visits': queryset
    }
    return render(request, "base.html", context)