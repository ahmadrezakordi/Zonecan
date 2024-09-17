from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView, DetailView

from .forms import *

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardView(LoginRequiredMixin, TemplateView):
        template_name = 'dashboard.html'


class EmployeeRegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class KelasorView(LoginRequiredMixin, View):
        def get(self, request):
            search_query = request.GET.get('search', '')

            if search_query:
                items = Kelasor.objects.filter(
                    Q(title__icontains=search_query)
                )
            else:
                items = Kelasor.objects.all()

            return render(request, 'kelasor.html', {"items": items})


class ParvandeView(LoginRequiredMixin, View):
    def get(self, request, pk):
        kelasor = get_object_or_404(Kelasor, pk=pk)

        search_query = request.GET.get('search', '')

        if search_query:
            items = Parvande.objects.filter(
                Q(title__icontains=search_query),
                kelasor=kelasor
            )
        else:
            items = Parvande.objects.filter(kelasor=kelasor)

        return render(request, 'parvande.html', {'items': items, "kelasor": kelasor})


class KelasorDetailView(LoginRequiredMixin, DetailView):
    model = Kelasor
    template_name = 'kelasor-detail.html'
    context_object_name = 'item'


class ParvandeDetailView(LoginRequiredMixin, DetailView):
    model = Parvande
    template_name = 'parvande-detail.html'
    context_object_name = 'item'


class KelasorCreateView(LoginRequiredMixin, CreateView):
    model = Kelasor
    form_class = KelassorForm
    template_name = 'kelasor-create.html'
    success_url = reverse_lazy('kelasor')
    context_object_name = 'item'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ParvandeCreateView(CreateView):
    model = Parvande
    form_class = ParvandeForm
    template_name = 'parvande-create.html'
    context_object_name = 'item'

    def get_success_url(self):
        # بررسی وجود self.object و self.object.kelasor
        if self.object and self.object.kelasor:
            return reverse('parvande-list', kwargs={'pk': self.object.kelasor.id})
        else:
            # اگر self.object یا self.object.kelasor وجود ندارد
            return reverse('parvande-list', kwargs={'pk': 1})  # مقدار پیش‌فرض مناسب

    def form_valid(self, form):
        kelasor = get_object_or_404(Kelasor, pk=self.kwargs['pk'])
        form.instance.kelasor = kelasor
        form.instance.user = self.request.user

        if 'file' in self.request.FILES:
            form.instance.file = self.request.FILES['file']

        return super().form_valid(form)


class KelasorUpdateView(LoginRequiredMixin, UpdateView):
    model = Kelasor
    form_class = KelassorForm
    template_name = 'kelasor-update.html'
    success_url = reverse_lazy('kelasor')
    context_object_name = 'item'


class ParvandeUpdateView(LoginRequiredMixin, UpdateView):
    model = Parvande
    form_class = ParvandeForm
    template_name = 'parvande-update.html'
    context_object_name = 'item'

    def get_success_url(self):
        # بررسی وجود self.object و self.object.kelasor
        if self.object and self.object.kelasor:
            return reverse('parvande-list', kwargs={'pk': self.object.kelasor.id})
        else:
            # اگر self.object یا self.object.kelasor وجود ندارد
            return reverse('parvande-list', kwargs={'pk': 1})  # مقدار پیش‌فرض مناسب

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs


class KelasorDeleteView(LoginRequiredMixin, DeleteView):
    model = Kelasor
    template_name = 'kelasor-delete.html'
    success_url = reverse_lazy('kelasor')
    context_object_name = 'item'


class ParvandeDeleteView(LoginRequiredMixin, DeleteView):
    model = Parvande
    template_name = 'parvande-delete.html'
    context_object_name = 'item'

    def get_success_url(self):
        # بررسی وجود self.object و self.object.kelasor
        if self.object and self.object.kelasor:
            return reverse_lazy('parvande-list', kwargs={'pk': self.object.kelasor.id})
        else:
            # اگر self.object یا self.object.kelasor وجود ندارد
            return reverse_lazy('parvande-list', kwargs={'pk': 1})  # مقدار پیش‌فرض مناسب
