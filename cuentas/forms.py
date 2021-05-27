from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields
from .models import UsuarioPers

class UsuarioPersCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPers
        fields = UserCreationForm.Meta.fields + ('edad',)

class UsuarioPersChangeForm(UserChangeForm):
    class Meta:
        model = UsuarioPers
        fields = UserChangeForm.Meta.fields