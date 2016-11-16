from django.shortcuts import render

from deployment.models import machine
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
# git

def list(request):
    queryset = machine.objects.all();
    queryset = serializers.serialize('json',queryset)
    return HttpResponse(queryset,content_type="application/json")

def hostname_query(request, hostname_id):
    queryset = machine.objects.get(hostname=hostname_id)
    queryset = serializers.serialize('json',queryset)
    return HttpResponse(queryset,content_type="application/json")

def generate_unattend_xml(request):
    
    template_vars['machines'] = machine.objects.all()
    