from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import PostForm

def index(request):
    return render(request, 'blog/index.html')

def blog_list(request):
    blogs = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog:blog_detail', pk=blog.pk)
    else:
        form = PostForm()
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def blog_update(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    if blog.author != request.user:
        return render(request, 'blog/not_owner.html')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_detail', pk=blog.pk)
    else:
        form = PostForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    if blog.author != request.user:
        return render(request, 'blog/not_owner.html')
    blog.delete()
    return redirect('blog:blog_list')

def blog_search(request, tag):
    blogs = Post.objects.filter(category__name=tag).order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})