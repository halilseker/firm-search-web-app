from django.urls import path

from .views import FirmListView, FirmDetailView, SearchResultsListView

urlpatterns = [
    path('', FirmListView.as_view(), name='firm_list'),
    path('<uuid:pk>', FirmDetailView.as_view(), name='firm_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
