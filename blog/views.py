from django.views.generic import DetailView, ListView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "post"
