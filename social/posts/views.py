from django.shortcuts import render, redirect
from .models import Post
from accounts.models import User
from .forms import AddPost
# Create your views here.
def all_posts(req):
    context = {
        'all_post': Post.objects.all(),
        'current_user': User.objects.get(is_current_user = True)
    }
    return render(req, 'index.html', context)

def add_post(req):
    if req.method == 'POST':
        description = req.POST.get('description')
        current_user = User.objects.get(is_current_user=True)
        new_post = Post(user=current_user, description=description)
        new_post.save()
        return redirect('all_post')
    context = {
        'add_form': AddPost()
    }
    return render(req, 'add_post.html', context)

def delete_post(req, id):
    found_post = Post.objects.get(id=id)
    found_post.delete()
    return redirect('all_post')

def likes(req, id):
    post = Post.objects.get(id=id)
    current_user = User.objects.get(is_current_user = True)
    if post.likes.filter(id=current_user.id).exists():
        post.likes.remove(current_user)
    else:
        post.likes.add(current_user)
    return redirect('all_post')