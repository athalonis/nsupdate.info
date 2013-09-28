# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings
from main.forms import *

class HomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['nav_home'] = True
        return context


class OverviewView(TemplateView):
    template_name = "main/overview.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OverviewView, self).get_context_data(*args, **kwargs)
        context['nav_overview'] = True
        context['WWW_IPV4_HOST'] = settings.WWW_IPV4_HOST
        context['WWW_IPV6_HOST'] = settings.WWW_IPV6_HOST
        context['session'] = self.request.session
        context['HostForm'] = HostForm(self.request.POST)
        if self.request.method == "POST":
            form = HostForm(self.request.POST)
            if form.is_valid():
                host = form.create_host()
                host.save()
            context['HostForm'] = form
        return context
