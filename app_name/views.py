# -*- coding: utf-8 -*-
from django.conf import settings
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http  import HttpResponse
from django.db.models import Q


def index(request, template_name = 'goodprice/index.html'):
    c = RequestContext(request )
    return render_to_response(template_name, c)    
