from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'trademaster/index.html', context=None)
        
class AboutPageView(TemplateView):
    template_name = "trademaster/about.html"