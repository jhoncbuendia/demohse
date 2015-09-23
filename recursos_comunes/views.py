from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template.context import RequestContext

# Create your views here.

def index(request):
    return render_to_response('recursos_comunes/base_dashboard.html', {}, context_instance=RequestContext(request))


def base_aplicaciones(request):
    return render_to_response('recursos_comunes/base_form.html', {}, context_instance=RequestContext(request))


def base_dashboard(request):
    return render_to_response('recursos_comunes/base_form.html', {}, context_instance=RequestContext(request))
