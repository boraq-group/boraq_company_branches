# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect, render, redirect, HttpResponse, HttpResponsePermanentRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings

def home_page(request):
	
	return render(request, "web/home.html", {})