from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Sautekfirm3


class Sautekfirm3ListView(ListView):
    model = Sautekfirm3
    context_object_name = 'firm_db_list' # new
    template_name = 'firm_db/firm_db_list.html'


class Sautekfirm3DetailView(DetailView):
    model = Sautekfirm3
    context_object_name = 'firm_db_detail' # new
    template_name = 'firm_db/firm_db_detail.html'


class SearchResultsListView(ListView):
    model = Sautekfirm3
    context_object_name = 'firm_db_list'
    template_name = 'firm_db/search_results.html'
    # queryset = Firm.objects.filter(firm_title__icontains='metal')

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Sautekfirm3.objects.filter(
            Q(firm_title__icontains= query) | Q(firm_services__icontains= query)
        )
