from django import forms


class PublisherForm(forms.Form):
    name = forms.CharField(max_length=64, label='Nazwa')
    city = forms.CharField(max_length=64, label='Miasto')