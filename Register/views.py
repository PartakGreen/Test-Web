from django.shortcuts import render, render_to_response
from django.template import RequestContext


def register(request):
    return render_to_response('reg.html',context_instance=RequestContext(request))