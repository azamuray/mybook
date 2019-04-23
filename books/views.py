from django.shortcuts import render
from .models import Book

def home(request):
	context = {
		'books': Book.objects.all()
	}
	return render(request, 'books/home.html', context)