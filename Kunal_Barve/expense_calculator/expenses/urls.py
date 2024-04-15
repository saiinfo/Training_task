from django.urls import path
from .views import ExpenditureListView, ExpenditureCreateView, ExpenditureDeleteView

urlpatterns = [
    path('', ExpenditureListView.as_view(), name='expenditure_list'),
    path('add/', ExpenditureCreateView.as_view(), name='add_expenditure'),
    path('remove/<int:pk>/', ExpenditureDeleteView.as_view(), name='remove_expenditure'),
]
