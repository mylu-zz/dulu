from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import RequestContext, loader

from shotgun_app.models import Users,Events,Attending, Friends

def index(request):
    template = loader.get_template('shotgun_app/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))