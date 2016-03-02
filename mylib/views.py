from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, PublishingPress
from .forms import BookForm
from django.utils import timezone
from django.views.generic.edit import CreateView

def home(request):
    return render(request, 'mylib/base.html')

def book_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'mylib/book_list.html', {'books': books, 'authors': authors})

def book_detail(request, pk):
    details = get_object_or_404(Book,pk=pk)
    books = Book.objects.all()
    authors = Author.objects.all()
    pubpresses = PublishingPress.objects.all()
    return render(request, 'mylib/book_detail.html', {'details': details, 'books': books, 'authors': authors, 'pubpresses': pubpresses})

"""def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        print(form)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.save_m2m()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'mylib/book_new.html', {'form': form})"""

class BookCreate(CreateView):
    model = Book
    template_name = 'mylib/book_new.html'
    fields = '__all__'

