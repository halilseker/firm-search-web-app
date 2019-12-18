from django.views.generic import ListView, DetailView

from .models import Firm


class FirmListView(ListView):
    model = Firm
    context_object_name = 'firm_list' # new
    template_name = 'firms/firm_list.html'


class FirmDetailView(DetailView):
    model = Firm
    context_object_name = 'firm' # new
    template_name = 'firms/firm_detail.html'
