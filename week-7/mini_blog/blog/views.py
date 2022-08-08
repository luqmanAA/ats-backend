import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin 
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import formats
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, FormMixin

from .forms import CommentModelForm
from .models import Author, Comment, Post

# Create your views here.

def index(request):
    """View function for home page of site."""
    
    # Generate counts of posts
    number_of_posts = Post.objects.all().count()
    
    # Generate counts of authors
    number_of_authors= Author.objects.count()
    
    context = {
        'number_of_posts': number_of_posts,
        'number_of_authors': number_of_authors,
    }
    # Render the HTML template index.html with the data in the context variable.   
    return render(request, 'index.html', context = context)

@login_required
def toggle_post(request, slug):
    try:
        post = Post.objects.get(slug=slug, author=request.user.id)
        post.is_deleted = not post.is_deleted
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Post.DoesNotExist:
        return HttpResponseRedirect(reverse('author-profile', args=[request.user.username]))


class BlogListView(ListView):
    model = Post
    # template_name = 'blog/blog_list.html'
    ordering = ['-post_date']
    paginate_by = 5
    
    def get_queryset(self):
        return Post.active_objects.all().order_by('-post_date')
    
    
# class BlogDetailView(FormMixin, DetailView):
#     model = Post
#     # template_name = 'blog/blog_detail.html'
#     form_class = CommentModelForm
#     # if self.request.method == 'POST':
    
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['comment_form'] = self.get_form()
#         return context_data
    

class BlogView(FormMixin, View):
    model = Post
    form_class = CommentModelForm
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment=''
        if request.user.id == post.author.id:
            comment = Comment.objects.filter(post=post) 
        else:
            comment = Comment.active_comments.filter(post=post)
        context = {
            'post': post,
            'comments': comment,
            'comment_form': self.get_form()
        }
        
        return render(request, 'blog/post_detail.html', context)
    
    @method_decorator(login_required)
    # def post(self, request, slug):
    #     post = Post.objects.filter(slug=slug).first()
    #     comment_form = CommentModelForm(request.POST)
    #     print(request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)    
    #         new_comment.post = post
    #         new_comment.comment_author = request.user
    #         new_comment.save()
    #         return HttpResponseRedirect(reverse('post-detail', args=[slug]))
    #     else:
    #         comment_form = CommentModelForm()
    #         return HttpResponseRedirect(reverse('post-detail', args=[slug]))
    def post(self, request, slug):
        response = json.load(request)
        post = Post.objects.filter(slug=slug).first()
        Comment.objects.create(
            description=response['description'],
            post=post,
            comment_author = request.user
        )
        comment = Comment.objects.filter(post=post).last()
        comment_time_formatted = formats.date_format(
            comment.comment_time, 'DATETIME_FORMAT'
        )
        response['id'] = comment.id
        response['author'] = str(comment.comment_author)
        response['timestamp'] = comment_time_formatted
        
        return JsonResponse(response)
  
    
class AuthorListView(ListView):
    model = Author
    template_name = 'blog/author_list.html'
    

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'blog/author_detail.html'


class CommentFormView(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ('description',)
    
    def get_queryset(self):
        return Post.objects.get(slug=self.kwargs['slug'])
    
    def get_context_data(self):
        context = super().get_context_data()
        context['post'] = self.get_queryset()
        return context
    
    
    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        form.instance.post = self.get_queryset()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('post-detail', kwargs={'slug': self.kwargs['slug'],})


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ('username', 'first_name', 'last_name', 'email', 'profile_image','bio')
    template_name_suffix = '_update_form'
    
    def get_queryset(self):
        return Author.objects.filter(id=self.request.user.id)
    
    def get_success_url(self) -> str:
        return reverse('author-profile', kwargs={'slug': self.kwargs['slug'],})
    

class AuthorProfileView(DetailView):
    model = Author
    template_name = 'blog/author_profile.html'
    context_object_name = 'author_profile'
    
    def get_context_data(self, **kwargs):
        author = Author.objects.get(slug = self.request.user.username)
        context = super().get_context_data(**kwargs)
        context['deleted_post'] = Post.deleted_objects.filter(author=author)
        return context
    

class PostEditView():
    pass


class CommentDeleteView(LoginRequiredMixin, View):
    
    def post(self, request, slug, pk):
        comment = Comment.objects.get(id=pk)
        comment.is_deleted = not comment.is_deleted
        comment.save()    
        return HttpResponseRedirect(reverse('post-detail', args=[slug]))