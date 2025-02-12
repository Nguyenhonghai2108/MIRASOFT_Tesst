from django.urls import path
from .views import AccountListCreateView, AccountDetailView, ShowSerialPasoView

urlpatterns = [
    path('api/accounts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('api/accounts/<int:registerID>/', AccountDetailView.as_view(), name='account-detail'),
    path('api/showSerialpaso/', ShowSerialPasoView.as_view(), name='show-serialpaso'),
]