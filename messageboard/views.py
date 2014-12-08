from django.shortcuts import render
from models import Topic

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
