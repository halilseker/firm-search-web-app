from django.urls import path

from .views import FirmListView, FirmDetailView

urlpatterns = [
    path('', FirmListView.as_view(), name='firm_list'),
    path('<int:pk>', FirmDetailView.as_view(), name='firm_detail'),
]
