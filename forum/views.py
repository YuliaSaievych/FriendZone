from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .form import CommentForm
from .models import Topic, Comment

def forum_feed(request):
    return render(request, 'forum/forum-feed.html')
def topic_list(request):
    topics = Topic.objects.all()
    total_topics = Topic.objects.count()

    return render(request, 'forum/topic_list.html', {'topics': topics, 'total_topics': total_topics},)


@login_required
def add_comment(request, pk):
    topic = get_object_or_404(Topic, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.created_by = request.user
            comment.save()
            return redirect('topic_detail', pk=pk)

    return redirect('topic_detail', pk=pk)


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    comments = topic.comments.all()
    form = CommentForm()
    return render(request, 'forum/topic_detail.html', {
        'topic': topic,
        'comments': comments,
        'form': form
    })