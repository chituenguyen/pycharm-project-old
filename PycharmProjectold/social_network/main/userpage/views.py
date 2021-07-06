from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    like_post = []
    for i in posts:
        is_like = Like.objects.filter(post=i, user=request.user)
        if is_like:
            like_post.append(i)
    data = {'posts': posts, 'like_post': like_post}
    return render(request, 'userpage/postfeed.html', data)


def post(request):
    if request.method == 'POST':
        image = request.FILES['image']
        caption = request.POST.get('caption', '')
        user = request.user
        print(image, caption, user)
        post_obj = Post(user=user, caption=caption, image=image)
        post_obj.save()

    return redirect('userpage:home')


def delPost(request, postId):
    post_ = Post.objects.filter(pk=postId)
    post_.delete()
    return redirect('userpage:home')


def userProfile(request, username):
    user = User.objects.filter(username=username)
    if user:
        profile = Profile.objects.get(user=user[0])
        bio = profile.bio
        post = getPost(user)
        connect = profile.connection
        follower = profile.follower
        following = profile.following
        userImage = profile.userImage
        for i in post:
            print(i)
        data = {'username': username, 'bio': bio, 'connect': connect, 'follower': follower,
                'following': following, 'userImage': userImage, 'post': post}
    else:
        return HttpResponse('no user')
    return render(request, 'userpage/userProfile.html', data)


def getPost(user):
    post_obj = Post.objects.filter(user__in=user)
    imgList = [post_obj[i:i + 3] for i in range(0, len(post_obj), 3)]
    return imgList


def LikePost(request, postId):
    post_ = Post.objects.get(pk=postId)
    user = request.user
    if Like.objects.filter(post=post_, user=user):
        Like.disliked(post_, user)
    else:
        Like.liked(post_, user)
    return redirect('userpage:home')


def Comment(request):
    if request.method == 'GET':
        comment_=request.GET.get('comment','')
        print(comment_)
    return render(request,'userpage/comment.html')
