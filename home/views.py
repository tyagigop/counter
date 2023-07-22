from django.shortcuts import render
from django.http import JsonResponse
from .models import DateNumberEntry
import json

# Create your views here.


def home(request):

    if request.method == 'POST':
        date_value = request.POST.get('date')
        number_value = int(request.POST.get('number'))

        try:
            entry = DateNumberEntry.objects.get(date=date_value)
            entry.number += number_value
            entry.save()
        except DateNumberEntry.DoesNotExist:
            entry = DateNumberEntry.objects.create(date=date_value, number=number_value)


    queryset = DateNumberEntry.objects.all()
    number = 0
    for query in queryset:
        number += query.number
    context = {
        'queryset' : queryset,
        'number' : number,
    }
    return render(request,'index.html',context)



