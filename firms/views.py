from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Firm


class FirmListView(ListView):
    model = Firm
    context_object_name = 'firm_list' # new
    template_name = 'firms/firm_list.html'


class FirmDetailView(DetailView):
    model = Firm
    context_object_name = 'firm' # new
    template_name = 'firms/firm_detail.html'


class SearchResultsListView(ListView):
    model = Firm
    context_object_name = 'firm_list'
    template_name = 'firms/search_results.html'
    # queryset = Firm.objects.filter(firm_title__icontains='metal')

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Firm.objects.filter(
            Q(firm_title__icontains= query) | Q(firm_services__icontains= query)
        )
