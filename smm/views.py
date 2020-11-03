from django.shortcuts import render,redirect
from smm.models import Post,BlogComment
from django.contrib import messages

# Create your views here.

def blog(request):
    post = Post.objects.all()
    return render(request,'smm/blog.html',{'post':post})

def post(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    return render(request,'blog/post.html',{'post':post,'comments':comments,'user':request.user})


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno=="":
            comment = BlogComment(comment=comment, user=user, post=post)
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

    return redirect(f"/smm/{post.slug}")