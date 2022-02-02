from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
#creating class based views

#home page view
class LandingPageView(generic.TemplateView):
    template_name = "index.html"

class LandingView(LoginRequiredMixin,generic.TemplateView):
    template_name = "landing.html"
