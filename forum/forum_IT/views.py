from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('view_posts')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def view_posts(request):
    posts = Post.objects.all()
    return render(request, 'view_posts.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def view_posts(request):
    posts = Post.objects.all().order_by('-created_at') 
    return render(request, 'view_posts.html', {'posts': posts})


def terms_view(request):
    return render(request, 'terms.html')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user != post.author:
        return HttpResponseForbidden()

    if request.method == "POST":
        post.delete()
        return redirect('view_posts')  

    return render(request, 'delete_confirm.html', {'post': post})