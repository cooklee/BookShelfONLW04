from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from bookshelf.forms import PublisherForm, AuthorForm
from bookshelf.models import Author, Publisher


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class AuthorCreateView(View):

    def get(self, request):
        form = AuthorForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            Author.objects.create(first_name=first_name, last_name=last_name)
            return redirect('authors')
        return render(request, 'form.html', {'form':form})


class AuthorListView(View):

    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'author_list.html', {'authors':authors})


class PublisherCreateView(View):

    def get(self, request):
        form = PublisherForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = PublisherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            Publisher.objects.create(name=name, city=city)
            return HttpResponse("Its OK")
        return render(request, 'form.html', {'form': form})
        # Author.objects.create(first_name=first_name, last_name=last_name)
        # return redirect('authors')