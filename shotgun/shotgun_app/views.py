from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import RequestContext, loader

from shotgun_app.models import Users,Events,Attending, Friends

def index(request):
    latest_event_list = Events.objects.all().order_by('-event_date')[:15]
    print latest_event_list
    latest_author_list = []
    for event in latest_event_list:
    	latest_author_list.append(Users.objects.get(pk = latest_event_list[0].author_id))
    print latest_author_list
    newsfeed = zip(latest_event_list, latest_author_list)
    print newsfeed
    for (event, user) in newsfeed:
    	print event.event_name
    user = Users.objects.get(pk=0)
    context = {
    	'latest_event_list': latest_event_list,
    	'user': user,
    	'newsfeed': newsfeed
    }
    return render(request, 'shotgun_app/index.html', context)