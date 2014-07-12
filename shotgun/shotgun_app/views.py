from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import RequestContext, loader

from shotgun_app.models import Users,Events,Attending, Friends

def index(request):
    latest_event_list = Events.objects.all().order_by('-event_date')[:15]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'shotgun_app/index.html', context)