from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, PostCreateForm
from django.contrib.auth import login, authenticate, logout
from .models import Post

#####################################################################################################
#        auth links                                                                                 #
#####################################################################################################

def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("feed")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('feed')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")

#####################################################################################################
#       base links                                                                                  #
#####################################################################################################

def homepage(request):
    tweets = Post.objects.all()
    context = {
        "tweets": tweets
    }
    return render(request, 'homepage.html', context)

def not_found(request):
    return render(request, '404.html')


#####################################################################################################
#       psot model links                                                                           #
#####################################################################################################

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'post_list.html', context)

def post_create(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.auther = request.user
            post.save()
            return redirect('feed')
    context = {
        "form": form
    }
    return redirect('feed')

def post_edit(request, post_id):
    form = PostCreateForm()
    post_obj = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostCreateForm(request.POST, instance=post_obj)
        if form.is_valid:
            form.save()
            return redirect('feed')
    context = {
        "form": form
    }
    return redirect('feed')

def post_delete(request, post_id):
    post_obj = Post.objects.get(id=post_id)
    post_obj.delete()
    return redirect('feed')

