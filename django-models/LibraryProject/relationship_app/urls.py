# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from .views import CustomLoginView, CustomLogoutView, register  
import relationship_app.views as views
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
   path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
   
   path('register/', views.register, name='register'),
     path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
   path('add_book/', views.add_book, name='add_book'),
    
  
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    
    
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
