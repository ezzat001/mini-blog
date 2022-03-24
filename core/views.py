from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Posts
from .serializers import PostsSerializer
from rest_framework import mixins
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.

class PostsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin ):
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
    
def index(request):
    context = {}
    if request.method == "POST":
        data = request.POST
        user=data.get('user')
        passw = data.get('pass')
        try:
            userauth = authenticate(username=user,password=passw)
            login(request,userauth)

        except:
            context = {'error': "Username or Password is incorrect" }
        
    posts = Posts.objects.filter(published=True)
    context = {"posts":posts}            
        
    return render(request, 'index.html',context)

def post_detail(request,id):
    post = Posts.objects.filter(id=id, published=True)
    post = post[0]
    context = {'post':post}
    return render(request, 'post_detail.html', context)

def author_posts(request,userid):
    
    posts = Posts.objects.filter(published=True,author=request.user)
    context = {'posts':posts}
    return render(request,'author.html',context)    

def logoutview(request):
    logout(request)
    
    return redirect('/')
    