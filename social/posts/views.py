from django.shortcuts import render, redirect
from .models import Post, Comment
from accounts.models import User
from .forms import AddPost
# Create your views here.
def all_posts(req):
    context = {
        'all_post': Post.objects.all(),
        'current_user': User.objects.get(is_current_user = True),
        'all_user': User.objects.all()
    }
    return render(req, 'index.html', context)

def add_post(req):
    if req.method == 'POST':
        description = req.POST.get('description')
        current_user = User.objects.get(is_current_user=True)
        new_post = Post(user=current_user, description=description, picture=req.FILES.get('picture'))
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

def comment(req, id):
    post = Post.objects.get(id=id)
    current_user = User.objects.get(is_current_user=True)

    if req.method == 'POST':
        comment_text = req.POST.get('comment')
        new_comment = Comment(comment=comment_text, post=post, user=current_user)
        new_comment.save()

    context = {
        'all_post': Post.objects.all(),
        'current_user': current_user,
        'comment': Comment.objects.filter(post=post),
        'comment_post': post,
    }
    return render(req, 'index.html', context)