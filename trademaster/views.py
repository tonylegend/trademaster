from django.shortcuts import render
from django.views.generic import TemplateView
from tradecompass.models import UserLog
from django.utils import timezone

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        userlogs = UserLog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'trademaster/index.html', {'userlogs': userlogs})
        
class AboutPageView(TemplateView):
    template_name = "trademaster/about.html"