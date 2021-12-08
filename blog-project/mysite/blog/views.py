from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,
                                    UpdateView,DeleteView)
from blog.forms import PostForm,CommentsForm
from django.urls import reverse_lazy
# Create your views here.

class AboutView(TemplateView):
    template_name = "blog/about.html"

#this will be the home page
class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now())
        # __lte filters posts with pusblish date less than or equal to current time


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    # reverse_lazy waits for the actual deletion to finish before redirecting


class DraftsListView(LoginRequiredMixin,ListView):
     login_url = '/login/'
     redirect_field_name = 'blog/post_draft_list.html'
     model = Post

     def get_queryset(self):
         return Post.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    # form = CommentsForm(request.POST or None)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentsForm()

    return render(request,'blog/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)



@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk)
    post_pk = comment.post.pk
    comment.Delete()
    return redirect('post_detail',pk=post_pk)
