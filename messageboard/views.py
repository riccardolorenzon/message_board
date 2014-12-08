from django.shortcuts import render, redirect
from models import Topic, Post
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def check_user_auth(user):
    if user.is_authenticated():
        return True
    else:
        return False

def index(request):
    topics = Topic.objects.all()
    ctx = {'topics': topics, 'user_login': check_user_auth(request.user)}
    return render(request, "topic-list.html", ctx)

def logout_view(request):
    logout(request)
    return redirect("main")

def sign_in(request):
    username= request.POST['username']
    password = request.POST['password']
    user=authenticate(username=username, password = password)
    if user is not None:
        login(request, user)
    return redirect('main')

def new_topic(request):
    topic_name=request.POST['topic_name']
    newTopic = Topic()
    newTopic.title = topic_name
    newTopic.save()
    return redirect('main')

def topic_detail(request, topic_id=None):
    topic = Topic.objects.get(id=topic_id)
    posts = topic.post_set.all()
    ctx = {'topic': topic, 'user_login': check_user_auth(request.user),
           'posts': posts}
    return render(request, 'topic-detail.html', ctx)

def add_post(request):
    post_content = request.POST['post-content']
    post_topic = Topic.objects.get(id=request.POST['topic_id'])
    newPost = Post()
    newPost.author = request.user
    newPost.content = post_content
    newPost.topic = post_topic
    newPost.save()
    return redirect('topic-detail', post_topic.id)

def delete_post(request):
    post_id = request.POST['post_id']
    delete_post_obj = Post.objects.get(id=post_id)
    topic_id = delete_post_obj.id
    delete_post_obj.delete()
    return redirect('topic-detail', topic_id = topic_id)