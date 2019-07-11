# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse as re  
# Create your views here.
def index(req):
	return re("<h2>cool dude</h2>")
