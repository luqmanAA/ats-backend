from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    # template = loader.get_template('portfolio/index.html')
    return render(request, 'portfolio/index.html')
    # return HttpResponse(template.render(request))

# class PortfolioView(TemplateView):
#     template_name = "my_portfolio/index.html"
