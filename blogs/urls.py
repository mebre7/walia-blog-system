from django.urls import path
from . import views

urlpatterns = [
    path('<int:cat_id>/', views.posts_by_category, name='category_detail'),
]