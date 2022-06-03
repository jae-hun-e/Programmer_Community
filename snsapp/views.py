from django.shortcuts import render, redirect,get_object_or_404
from .forms import PostForm, CommentForm, FreePostForm, FreeCommentForm
from .forms import Post, FreePost


def home(req):
    # posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(req, 'index.html', {'posts': posts})


def postcreate(req):
    # req가 post일 경우
    if req.method == 'POST' or req.method == "FIlES":
        form = PostForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PostForm()
    return render(req, 'post_form.html', {'form': form})


def detail(req, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(req, 'detail.html', {'post_detail': post_detail, 'comment_form': comment_form})


def new_comment(req, post_id):
    filled_form = CommentForm(req.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)  # 아직 저장ㄴㄴ
        finished_form.post = get_object_or_404(Post, pk=post_id)  # post와 연결
        finished_form.save()  # 이제 저장
    return redirect('detail', post_id)


def freehome(request):
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})


def freepostcreate(request):
    if request.method == 'POST' or request.method == "FILES":
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            form.save()
            return redirect('freehome')

    else:
        form = PostForm()
    return render(request, 'free_post_form.html', {'form': form})


def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail': post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)
