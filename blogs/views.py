from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db.models import Q
from blogs.models import Blog, Category


# Create your views here.
def posts_by_category(request, cat_id):
    category = Category.objects.filter(id=cat_id).first()
    if not category:
        return render(request, '404.html', status=404)

    posts = Blog.objects.filter(category=category, status=1)
    other_categories = Category.objects.exclude(id=category.id)
    context = {
        'category': category,
        'posts': posts,
        'other_categories': other_categories,
        'post_count': posts.count(),
    }
    return render(request, 'posts_by_category.html', context)


@login_required(login_url='login')
def blog_detail(request, slug: str):
    blog = Blog.objects.filter(slug=slug, status=1).first()
    if not blog:
        blog = next((item for item in Blog.objects.filter(status=1) if slugify(item.title) == slug), None)
    if not blog:
        return render(request, '404.html', status=404)

    related_posts = Blog.objects.filter(
        category=blog.category,
        status=1,
    ).exclude(pk=blog.pk)[:3]
    other_categories = Category.objects.exclude(id=blog.category.id)

    context = {
        'blog': blog,
        'category': blog.category,
        'related_posts': related_posts,
        'other_categories': other_categories,
    }
    return render(request, 'blog_detail.html', context)


def search(request):
    query = request.GET.get('q', '').strip()
    filter_type = request.GET.get('filter', 'all').lower()

    results = []

    if query:
        if filter_type == 'all':
            # Search across all fields
            results = Blog.objects.filter(
                Q(title__icontains=query) |
                Q(short_description__icontains=query) |
                Q(blog_body__icontains=query) |
                Q(category__name__icontains=query) |
                Q(author__username__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query),
                status=1
            ).distinct().order_by('-created_at')

        elif filter_type == 'blog':
            # Search in title, short_description, blog_body (content)
            results = Blog.objects.filter(
                Q(title__icontains=query) |
                Q(short_description__icontains=query) |
                Q(blog_body__icontains=query),
                status=1
            ).distinct().order_by('-created_at')

        elif filter_type == 'topic':
            # Search only in title
            results = Blog.objects.filter(
                title__icontains=query,
                status=1
            ).order_by('-created_at')

        elif filter_type == 'category':
            # Search in category name
            results = Blog.objects.filter(
                category__name__icontains=query,
                status=1
            ).order_by('-created_at')

        elif filter_type == 'author':
            # Search by username (first), then first_name, then last_name
            username_results = Blog.objects.filter(
                author__username__icontains=query,
                status=1
            ).order_by('-created_at')

            firstname_results = Blog.objects.filter(
                author__first_name__icontains=query,
                status=1
            ).exclude(pk__in=username_results.values_list('pk', flat=True)).order_by('-created_at')

            lastname_results = Blog.objects.filter(
                author__last_name__icontains=query,
                status=1
            ).exclude(pk__in=username_results.values_list('pk', flat=True)).exclude(
                pk__in=firstname_results.values_list('pk', flat=True)
            ).order_by('-created_at')

            results = list(username_results) + list(firstname_results) + list(lastname_results)

    context = {
        'query': query,
        'posts': results,
        'filter_type': filter_type,
    }
    return render(request, 'search.html', context)
