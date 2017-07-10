from django.shortcuts import render
from django.views.generic import CreateView, DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import UserCreationForm

from django.core.urlresolvers import reverse_lazy

class CreateUserView(CreateView):
    model = User
    template_name = 'new.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')


class Porfile(DetailView,LoginRequiredMixin):
    model = User
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user

class EditProfileVView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'edit.html'
    fields = ['username', 'name', 'email', 'avatar']
    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(EditProfileVView, self).get_context_data(**kwargs)
        context['avatars'] = ['default', 'elyse', 'eve', 'kristy', 'lena', 'mark', 'matthew', 'molly', 'rachel']
        return context

signin = CreateUserView.as_view()
profile = Porfile.as_view()
edit_profile = EditProfileVView.as_view()
