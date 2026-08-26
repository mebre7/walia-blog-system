from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    tagline = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/category_images/', null=True, blank=True)
    short_code = models.CharField(max_length=4, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.short_code:  # Only auto-generate if it's empty
            words = self.name.split()
            if len(words) > 1:
                # Take first letter of each word and join them
                self.short_code = "".join([word[0].upper() for word in words])[:5]
            else:
                # Take just the first letter
                self.short_code = self.name[0].upper()
        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
STATUS_CHOICES = (
    (0, 'Draft'),
    (1, 'Published')
)
class Blog(models.Model):
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs') # this is used to link the blog to the category and also to get all blogs under a category using category.blogs.all()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    short_description = models.TextField(max_length=500, null=False)
    blog_body = models.TextField(null=False)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Blog.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title