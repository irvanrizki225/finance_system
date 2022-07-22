from django.urls import URLPattern, path
from .views import TransactionListView,TransactionCreateView,TransactionUpdateView,TransactionDeleteView

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction'),
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
    # path('detail/<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('update/<int:pk>/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'),
]