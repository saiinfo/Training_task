from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Expenditure

class ExpenditureListView(ListView):
    model = Expenditure
    template_name = 'expenses/expenditure_list.html'
    context_object_name = 'expenditures'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_expenditure'] = sum(expenditure.amount for expenditure in self.object_list)
        return context

class ExpenditureCreateView(CreateView):
    model = Expenditure
    template_name = 'expenses/add_expenditure.html'
    fields = ['description', 'amount']
    success_url = reverse_lazy('expenditure_list')

class ExpenditureDeleteView(DeleteView):
    model = Expenditure
    success_url = reverse_lazy('expenditure_list')
