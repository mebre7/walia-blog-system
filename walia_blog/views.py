from django.shortcuts import render
from blogs.models import Blog,Category
import random

def home(request):
    # contexts are in context_processors
    return render(request, 'home.html')


def custom_404(request, exception=None):
    """Custom 404 handler that renders the project's `404.html` template.

    Django will call this view when a page is not found and `DEBUG` is False.
    The signature accepts the optional `exception` parameter matching Django's handler requirement.
    """
    return render(request, '404.html', status=404)
