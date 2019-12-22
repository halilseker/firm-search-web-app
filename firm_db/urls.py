from django.urls import path

from .views import Sautekfirm3ListView, Sautekfirm3DetailView, SearchResultsListView

urlpatterns = [
    path('', Sautekfirm3ListView.as_view(), name='firm_db_list'),
    path('<int:pk>', Sautekfirm3DetailView.as_view(), name='firm_db_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
