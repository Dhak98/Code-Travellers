from django.shortcuts import render

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'myapp/index.html', {'posts': posts})