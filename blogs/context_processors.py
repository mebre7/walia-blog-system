from .models import Blog, Category
import random
from django.db.models import Q
def get_categories(request):
    # for searching
    query = request.GET.get('q', '')
    query = query.strip() if query is not None else ''

    results = Blog.objects.filter(status=1).filter(
        Q(title__icontains=query) |
        Q(short_description__icontains=query) |
        Q(blog_body__icontains=query) |
        Q(author__username=query) |
        Q(author__first_name__icontains=query) |
        Q(author__last_name__icontains=query) |
        Q(category__name__icontains=query)
    ).distinct().order_by('-created_at')

    # for categories
    all_categories = Category.objects.all()
    trending_post = Blog.objects.filter(status=1, is_featured=True).order_by('-created_at').first()
    featured_posts = Blog.objects.filter(is_featured=True, status=1)

    if trending_post:
        featured_posts = featured_posts.exclude(pk=trending_post.pk)

    featured_posts = featured_posts.order_by('-created_at')[:5]
    all_blogs = Blog.objects.filter(status=1, is_featured=False).order_by('-created_at')
    context = {
        # for searching
        'results': results,
        'query': query,
        'posts': results,
        # for categories
        'featured_posts': featured_posts,
        'all_blogs': all_blogs,
        'trending_post': trending_post,
        'all_categories': list(all_categories),
        'selected_categories': random.sample(list(all_categories), min(len(all_categories), 6))
    }
    return context