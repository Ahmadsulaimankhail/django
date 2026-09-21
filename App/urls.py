from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('prograss/', views.prograss, name='Prograss'),

    path('book/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),

    path('lending/', views.lendingBook, name='Lending'),
    path('lended/', views.show_lendedBook, name='lended'),

    path('members/', views.showMember, name='showMember'),
    path('addMember/', views.addMember, name='member'),

    path('return/', views.returnBook, name='returnBook'),

    # You were missing this
    path(
        'returnsearch/',
        views.returnbook_search,
        name='returnbook_search'
    ),

    path(
        'return-remove/<int:bookid>/',
        views.return_remove_add,
        name='return_remove_add'
    ),
]