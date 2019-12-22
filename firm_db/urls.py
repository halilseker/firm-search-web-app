from django.urls import path

from .views import CompanyListView, CompanyDetailView, SearchResultsListView

urlpatterns = [
    path('', CompanyListView.as_view(), name='firm_db_list'),
    path('<int:pk>', CompanyDetailView.as_view(), name='firm_db_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
