from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class AboutView(TemplateView):
    template_name = "conditons_page.html"
