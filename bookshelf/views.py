from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from bookshelf.models import Author


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class AuthorCreateView(View):

    def get(self, request):
        return render(request, 'author_add.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Author.objects.create(first_name=first_name, last_name=last_name)
        return redirect('authors')


class AuthorListView(View):

    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'author_list.html', {'authors':authors})