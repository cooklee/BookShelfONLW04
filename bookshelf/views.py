
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.base import View

from bookshelf.forms import PublisherForm, AuthorForm, BookForm
from bookshelf.models import Author, Publisher, BookReview, Book


class IndexView(View):

    def get(self, request):
        zmienna = request.GET.get('pies', '')
        return render(request, 'base.html', {'z':zmienna})


class AuthorCreateView(View):

    def get(self, request):
        form = AuthorForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            Author.objects.create(first_name=first_name, last_name=last_name)
            return redirect('authors')
        return render(request, 'form.html', {'form': form})


class AuthorListView(View):

    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'author_list.html', {'authors': authors})


class PublisherCreateView(View):

    def get(self, request):
        form = PublisherForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = PublisherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            Publisher.objects.create(name=name, city=city)
            return HttpResponse("Its OK")
        return render(request, 'form.html', {'form': form})


class BookCreateView(View):

    def get(self, request):
        form = BookForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'form.html', {'form': form})

class ListBookView(ListView):
    model = Book
    template_name = 'list_view.html'


class UpdateBookView(UpdateView):
    model = Book
    fields = "__all__"
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('update_book', args=(self.object.pk, ))





class BookReviewCreateView(CreateView):
    model = BookReview
    fields = ['book', 'text', 'rate']
    template_name = 'form.html'
    success_url = reverse_lazy('index')


    def get_success_url(self):
        return reverse('index') + "?pies=reksio"
