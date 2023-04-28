
from django.urls import path
from .views import BlogPostView, BlogPostCreate


urlpatterns = [
    path('blog/', BlogPostView.as_view(), name = 'blog'),
    path('blog-create/', BlogPostCreate.as_view(), name = 'blog-create'),
]