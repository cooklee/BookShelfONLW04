from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='hasło')
    password2 = forms.CharField(widget=forms.PasswordInput(),  label='Powtórz Hasło')

    def clean(self):
        data = super().clean()
        password1 = data.get("password1", '')
        password2 = data.get("password2", '')
        if password1 != password2:
            raise ValidationError('Hasła musza być takie same')
        return data

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']
        labels = {
            'username': 'nazwa użytkownika',
        }
        help_texts = {
            'username':'',
            'first_name':"abrakadabra"
        }
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'username'})
        }