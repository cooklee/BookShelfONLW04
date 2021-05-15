from django import forms
from django.core.exceptions import ValidationError

from bookshelf.models import Book


def check_if_first_is_big(value):
    if value[0].isupper():
        return True
    raise ValidationError('Zaczynamy wieką literą')



class PublisherForm(forms.Form):
    name = forms.CharField(max_length=64, label='Nazwa')
    city = forms.CharField(max_length=64, label='Miasto')


class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=4, validators=[check_if_first_is_big])
    last_name = forms.CharField(max_length=4, validators=[check_if_first_is_big, ])

    def clean(self):
        data = super().clean()
        if len(data.get('first_name', ''))+len(data.get('last_name', ''))> 6:
            raise ValidationError("Hola hola wstrzymaj konie max 6 znaków")
        return data


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

