# plik biblioteka/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('books/update_delete/<int:pk>/', views.book_update_delete),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/nazwisko/<str:name>/', views.osoba_name_filter_url),
    path('osoby/nazwisko_param', views.osoba_name_filter_params), #NIE DAJEMY "/" NA KONIEC URI
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),
    #ClassBasedViews
    # path("books_vbs/", views.BookListView.as_view(), name="book-list"),
    # path("books_vbs/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    # path('osoby_vbs/', views.OsobaListAPIView.as_view()),
    # path('osoby_vbs/<int:pk>/', views.OsobaDetailAPIView.as_view()),
    # path('osoby_vbs/nazwisko/<str:name>/', views.OsobaSearchAPIView.as_view()),
    # path('osoby_vbs/nazwisko', views.OsobaNameFilterView.as_view()),
    # path('stanowiska_vbs/', views.StanowiskoListAPIView.as_view()),
    # path('stanowiska_vbs/<int:pk>/', views.StanowiskoDetailAPIView.as_view()),
    #HTML Views
    path('welcome/', views.welcome_view),
    path("html/osoby/", views.osoba_list_html, name="osoba-list"),
    path("html/osoby/<int:id>/", views.osoba_detail_html, name="osoba-detail"),
    path("html/osoby/dodaj/", views.osoba_create_html, name="osoba-create"),
    path("html/osoby/dodaj_django/", views.osoba_create_django_form, name="osoba-create-django"),
    # Lab 8 (B)
    ## Zad 1
    path("html/books/", views.book_list_html, name = "book-list"),
    path("html/books/<int:id>/", views.book_detail_html, name = "book-detail"),
    path("html/stanowiska/", views.stanowisko_list_html, name = "stanowisko-list"),
    path("html/stanowiska/<int:id>/", views.stanowisko_detail_html, name = "stanowisko-detail"),
    ## Zad 2
    path("html/books/dodaj/", views.book_create, name = "book-create"),
    path("html/stanowiska/dodaj/", views.stanowisko_create, name = "stanowisko-create"),
    ## Zad 3
    path("html/osoby/szukaj/", views.osoba_name_search, name = "osoba-search-name"),
    ## Zad 5
    path('html/osoby/<int:id>/edit/', views.osoba_edit, name='osoba-edit'),
    # ============= Lab 9 ===================
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('token/login/', views.drf_token_login, name='drf-token-login'),
    path('token/logout/', views.drf_token_logout, name='drf-token-logout'),
    # Zadania lab 9
    path("html/osoby/wlasciciel/", views.osoba_list_owner, name = "osoba-list-owner"),
    path("osoby/<int:pk>/edytuj/", views.osoba_update, name = "osoba-update-drf"),
    path("osoby/<int:pk>/usun/", views.osoba_delete, name = "osoba-delete-drf"),
    path("html/stanowiska/<int:pk>/members/", views.osoba_stanowisko, name = "osoba-stanowisko"),
    # ============= Lab 10 ===================
    path("osoby/<int:pk>/permisje/", views.osoba_view),
    path("osoby/<int:pk>/permisje_decorator/", views.osoba_view_decorator),
]