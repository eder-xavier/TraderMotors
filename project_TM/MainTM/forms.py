from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=255, required=True)
    telefone = forms.CharField(required=False)
    endereco = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ['nome_completo', 'username', 'email', 'telefone', 'endereco', 'password1', 'password2']
