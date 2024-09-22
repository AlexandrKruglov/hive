from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, DetailView

from honeycombs.forms import HoneycombsForm
from honeycombs.models import Honeycombs


# Create your views here.
class HoneycombsPageVeiw(TemplateView):
    template_name = 'honeycombs/start.html'


class HoneycombsCreateView(CreateView):
    model = Honeycombs
    form_class = HoneycombsForm
    success_url = reverse_lazy('honeycombs:lk')

    def form_valid(self, form):
        honeycombs_form = form.save()
        user = self.request.user
        honeycombs_form.owner = user
        honeycombs_form.save()
        return super().form_valid(form)


class HoneycombsUpdateView(UpdateView):
    model = Honeycombs
    form_class = HoneycombsForm
    success_url = reverse_lazy('honeycombs:lk')


class HoneycombsListView(ListView):
    model = Honeycombs
    template_name = 'honeycombs/home.html'


class ProfileListView(ListView):
    model = Honeycombs
    template_name = 'honeycombs/lk.html'


class HoneycombsDetailView(DetailView):
    model = Honeycombs


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Honeycombs
    success_url = reverse_lazy('honeycombs:lk')
