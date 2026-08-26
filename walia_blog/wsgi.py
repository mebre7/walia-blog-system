import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'walia_blog.settings')

application = get_wsgi_application()

# Required by Vercel serverless function runtime
app = application
