from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, TweetCreateForm
from django.contrib.auth import login, authenticate, logout
from .models import Post

#####################################################################################################
#        auth links                                                                                 #
#####################################################################################################

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            # redirect the user to the homepage after successful register
            return redirect('homepage')
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # redirect the user to the homepage after successful login
                return redirect('homepage')
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)

def signout(request):
    logout(request)
    return redirect("login")

#####################################################################################################
#       tweets model links                                                                          #
#####################################################################################################

def homepage(request):
    tweets = Post.objects.all()
    context = {
        "tweets": tweets
    }
    return render(request, 'homepage.html', context)

def create_tweet(request):
    form = TweetCreateForm()
    if request.method == "POST":
        form = TweetCreateForm(request.POST)
        if form.is_valid:
            form.save(commit=False)
            form.auther = request.user
            form.save()
            return redirect('homepage')
    context = {
        "form": form
    }
    return redirect('homepage')

def edit_tweet(request, tweet_id):
    form = TweetCreateForm()
    post_obj = Post.objects.get(id=tweet_id)
    if request.method == "POST":
        form = TweetCreateForm(request.POST, instance=post_obj)
        if form.is_valid:
            form.save()
            return redirect('homepage')
    context = {
        "form": form
    }
    return redirect('homepage')

def delete_tweet(request, tweet_id):
    post_obj = Post.objects.get(id=tweet_id)
    post_obj.delete()
    return redirect('homepage')
