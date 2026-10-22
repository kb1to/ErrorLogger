from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Log, Idea, Post
from .forms import LogForm, IdeaForm, PostForm

@login_required
def dashboard(request):
    query = request.GET.get('q', '')
    
    if query:
        logs = Log.objects.filter(Q(problem_name__icontains=query) | Q(what_i_didnt_know__icontains=query) | Q(solution__icontains=query))
        ideas = Idea.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        posts = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    else:
        logs = Log.objects.all()
        ideas = Idea.objects.all()
        posts = Post.objects.all()

    stats = {
        'total_logs': Log.objects.count(),
        'total_ideas': Idea.objects.count(),
        'ideas_acted_on': Idea.objects.filter(acted_on_it=True).count(),
    }

    context = {
        'logs': logs,
        'ideas': ideas,
        'posts': posts,
        'stats': stats,
        'query': query
    }
    return render(request, 'log/dashboard.html', context)

@login_required
def create_log(request):
    form = LogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'log/create_form.html', {'form': form, 'title': 'New Error Log', 'cancel_url': 'dashboard'})

@login_required
def create_idea(request):
    form = IdeaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'log/create_form.html', {'form': form, 'title': 'New Idea', 'cancel_url': 'dashboard'})

@login_required
def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'log/create_form.html', {'form': form, 'title': 'New Post', 'cancel_url': 'dashboard'})

@login_required
def edit_log(request, pk):
    log = get_object_or_404(Log, pk=pk)
    form = LogForm(request.POST or None, instance=log)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'log/create_form.html', {'form': form, 'title': 'Edit Error Log', 'cancel_url': 'dashboard'})

@login_required
def edit_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    form = IdeaForm(request.POST or None, instance=idea)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'log/create_form.html', {'form': form, 'title': 'Edit Idea', 'cancel_url': 'dashboard'})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'log/create_form.html', {'form': form, 'title': 'Edit Post', 'cancel_url': 'dashboard'})

@login_required
def delete_log(request, pk):
    log = get_object_or_404(Log, pk=pk)
    log.delete()
    return redirect('dashboard')

@login_required
def delete_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    return redirect('dashboard')

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('dashboard')
