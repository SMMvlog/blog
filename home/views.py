from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from smm.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    post = Post.objects.all()
    return render(request,'home/home.html',{'post':post})

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<5 or len(phone)<10 or len(content)<10:
            messages.error(request, "Please fill the form correctly")
                
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request,'home/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        post=Post.objects.none()
    else:
        postTitle= Post.objects.filter(title__icontains=query)
        postAuthor= Post.objects.filter(author__icontains=query)
        postContent =Post.objects.filter(content__icontains=query)
        post=  postTitle.union(postContent, postAuthor)
    if post.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'post': post, 'query': query}
    return render(request, 'home/search.html', params)

def Login(request):
    if request.method == "POST":
            # Get the post parameters
        usernamel = request.POST['usernamel']
        passwordl = request.POST['passwordl']

        user = authenticate(username=usernamel, password=passwordl)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials or may be you havn't signup yet! Please try again or signup")
            return redirect("home")

        return HttpResponse("404- Not found")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        password1 = request.POST['password1']

        if (len(username) < 5) or (len(username) > 10 ) :
            messages.error(request, " Your user name must be betwwen 5 an 10 chracters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (password != password1):
            messages.error(request, " Passwords do not match")
            return redirect('home')


        myuser =User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

    return HttpResponse("login")

def about(request):
    return render(request,'home/about.html')



