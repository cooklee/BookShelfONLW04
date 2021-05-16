"""BookShelfOnl4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookshelf import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(), name='index'),
    path("add_author/", views.AuthorCreateView.as_view(), name='add_author'),
    path("authors/", views.AuthorListView.as_view(), name='authors'),
    path("add_publisher/", views.PublisherCreateView.as_view(), name='add_publisher'),
    path("add_book/", views.BookCreateView.as_view(), name='add_book'),
    path("update_book/<int:pk>/", views.UpdateBookView.as_view(), name='update_book'),
    path("book_list/", views.ListBookView.as_view(), name='book_list'),
    path("add_review/", views.BookReviewCreateView.as_view(), name='add_bookreview'),
    ####################################################################################
    path("accounts/login/", accounts_views.LoginView.as_view(), name='login'),
    path("accounts/logout/", accounts_views.LogOutView.as_view(), name='logout'),
    path("accounts/register/", accounts_views.CreateUserView.as_view(), name='register'),
]


