from django import forms


class PublisherForm(forms.Form):
    name = forms.CharField(max_length=64)
    city = forms.CharField(max_length=64)