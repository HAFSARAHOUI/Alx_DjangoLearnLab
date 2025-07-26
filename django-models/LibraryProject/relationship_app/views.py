from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import  redirect
from django.contrib.auth import login  
from django.contrib.auth.forms import UserCreationForm 
from .models import Book
from .models import Library
# Create your views here.
# relationship_app/views.py

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# عرض تسجيل الخروج
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# عرض التسجيل
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('login') 
    else:
        form = UserCreationForm() 
    return render(request, 'relationship_app/register.html', {'form': form})

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})
# relationship_app/views.py
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
