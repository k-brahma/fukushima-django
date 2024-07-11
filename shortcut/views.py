from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from shortcut.models import Example


# Create your views here.
class WellComeView(TemplateView):
    template_name = 'shortcut/welcome.html'


class ExampleListView(ListView):
    model = Example
    template_name = 'shortcut/example_list.html'


class ExampleDetailView(DetailView):
    model = Example
    template_name = 'shortcut/example_detail.html'


class ExampleCreateView(CreateView):
    model = Example
    template_name = 'shortcut/example_form.html'
    fields = ['operation', 'result', 'description']
    success_url = '/shortcut/example/'


class ExampleUpdateView(UpdateView):
    model = Example
    template_name = 'shortcut/example_form.html'
    fields = ['operation', 'result', 'description']
    success_url = '/shortcut/example/'


class ExampleDeleteView(DeleteView):
    model = Example
    template_name = 'shortcut/example_confirm_delete.html'
    success_url = '/shortcut/example/'
