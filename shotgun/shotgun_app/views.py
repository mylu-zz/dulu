from django.shortcuts import render
from django.template import RequestContext, loader
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from shotgun_app.models import Users,Events,Attending, Friends
import datetime

def index(request):
    latest_event_list = Events.objects.all().order_by('-publish_time')[:15]
    latest_author_list = []
    for event in latest_event_list:
    	latest_author_list.append(Users.objects.get(pk = latest_event_list[0].author_id))
    newsfeed = zip(latest_event_list, latest_author_list)
    user = Users.objects.get(pk=1)
    context = {
    	'latest_event_list': latest_event_list,
    	'user': user,
    	'newsfeed': newsfeed
    }
    return render(request, 'shotgun_app/index.html', context)

def create(request):
    return render(request, 'shotgun_app/create.html')

def create_handler(request):
    if 1:
        name = request.POST['ename']
        description = request.POST['edescription']
        location = request.POST['location']
        privacy = request.POST['privacy']
        if request.POST['etime'] and request.POST['edate']:
            time = request.POST['etime'].split(':')
            date = request.POST['edate'].split('-')
            time = [int(x) for x in time]
            date = [int(x) for x in date]
            edatetime = datetime.datetime(year=date[0],month=date[1],day=date[2],hour=time[0],minute=time[1])
        else:
            edatetime = None
        if not location:
            location = ''
        user = Users.objects.get(pk=1)
        e = Events(event_name=name, event_description=description, author_id=user.user_id, publish_time=timezone.now(), location=location,privacy=privacy,event_time=edatetime)
        e.save()
        return index(request)
   
