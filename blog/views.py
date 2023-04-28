from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import BlogPost

# Create your views here.
class BlogPostView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'

class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'blog_create.html'
    fields = ["title", "description"]
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogPostCreate, self).form_valid(form)