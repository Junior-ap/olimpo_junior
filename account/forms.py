from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

#qualquer usuario pode criar
class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

#criar pelo django admin
class UserAdninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']
