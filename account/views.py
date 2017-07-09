from django.shortcuts import render
from django.views.generic import CreateView

from .models import User
from .forms import UserCreationForm

from django.core.urlresolvers import reverse_lazy

class CreateUserView(CreateView):
    model = User
    template_name = 'new.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')

signin = CreateUserView.as_view()
