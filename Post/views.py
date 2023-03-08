from django.shortcuts import render,redirect,get_object_or_404
from django.core import mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import About,Subscribe,Post,Postcads,Category,Contact
from django.core.mail import send_mail
from kblog import settings


# Create your views here.
def index(request):
    keyword = request.GET.get("q")
    posts = Post.objects.all()[:12]
    categories = Category.objects.all()
    context = {
        'posts':posts,
        'categories':categories,
    }

    if keyword:
        dey = "Axtarşın nəticəsi"
        s = 0
        posts = Post.objects.filter(title__contains = keyword)
        for i in posts:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        context = {
        'posts':posts,
        'categories':categories,
        'dey':dey,
        }
        return render(request,"search.html",context)
    try:
        subs = request.POST.get("subscribe")
        newsubs = Subscribe(email = subs)
        newsubs.save()
    except:
        pass
    return render(request,"index.html",context)

def category(request,slug):
    keyword = request.GET.get("q")
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarşın nəticəsi"
        s = 0
        posts = Post.objects.filter(title__contains = keyword)
        for i in posts:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        context = {
        'posts':posts,
        'categories':categories,
        'dey':dey,
        }
        return render(request,"search.html",context)
    category = Category.objects.filter(slug=slug).first()
    posts_lists = Post.objects.filter(category=category)
    paginator = Paginator(posts_lists,12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts':posts,
        'categories':categories,
        'category':category,
    }
    try:
        subs = request.POST.get("subscribe")
        newsubs = Subscribe(email = subs)
        newsubs.save()
    except:
        pass
    return render(request,"category.html",context)

def post_detail(request,slug):
    keyword = request.GET.get("q")
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarşın nəticəsi"
        s = 0
        posts = Post.objects.filter(title__contains = keyword)
        for i in posts:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        context = {
        'posts':posts,
        'categories':categories,
        'dey':dey,
        }
        return render(request,"search.html",context)
    post = get_object_or_404(Post,slug=slug)
    context = {
        'post':post,
        'categories':categories,
    }
    try:
        subs = request.POST.get("subscribe")
        newsubs = Subscribe(email = subs)
        newsubs.save()
    except:
        pass
    return render(request,"detail.html",context)


def about(request):
    keyword = request.GET.get("q")
    categories = Category.objects.all()
    cat = Category.objects.all()[:1]
    about = About.objects.all()
    context = {
        'categories':categories,
        'about':about,
        'cat':cat,
    }
    if keyword:
        dey = "Axtarşın nəticəsi"
        s = 0
        posts = Post.objects.filter(title__contains = keyword)
        for i in posts:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        context = {
        'posts':posts,
        'categories':categories,
        'cat':cat,
        'dey':dey,
        }
        return render(request,"search.html",context)
    try:
        subs = request.POST.get("subscribe")
        newsubs = Subscribe(email = subs)
        newsubs.save()
    except:
        pass
    return render(request,"about.html",context)

def potcast(request):
    keyword = request.GET.get("q")
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarşın nəticəsi"
        s = 0
        posts = Post.objects.filter(title__contains = keyword)
        for i in posts:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        context = {
        'posts':posts,
        'categories':categories,
        'dey':dey,
        }
        return render(request,"search.html",context)
    posts_lists = Postcads.objects.filter()
    paginator = Paginator(posts_lists,12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts':posts,
        'categories':categories,
        'category':category,
    }
    try:
        subs = request.POST.get("subscribe")
        newsubs = Subscribe(email = subs)
        newsubs.save()
    except:
        pass
    return render(request,"potcast.html",context)

def contact(request):
    keyword = request.GET.get("q")
    posts = Post.objects.all()[:12]
    categories = Category.objects.all()
    context = {
        'posts':posts,
        'categories':categories,
    }
    if keyword:
        dey = "Axtarşın nəticəsi"
        s = 0
        posts = Post.objects.filter(title__contains = keyword)
        for i in posts:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        context = {
        'posts':posts,
        'categories':categories,
        'dey':dey,
        }
        return render(request,"search.html",context)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        phone = request.POST.get("phone")
        text = request.POST.get("text")
        newcontact = Contact(name = name, email = email, subject = subject,phone = phone, text = text)
        newcontact.save()
    try:
        subs = request.POST.get("subscribe")
        newsubs = Subscribe(email = subs)
        newsubs.save()
    except:
        pass
    return render(request,"contact.html",context)

def subscribe(request,slug):
    subs = Subscribe.objects.all()
    post = get_object_or_404(Post, slug = slug)
    for i in subs:
        email = i.email
        subject = post.title
        message = "Mənim "+ "'"+ post.title + "'"+ " adlı məqaləmlə tanış olmaq üçün linkə toxunun: " + "https://kamransaleh.net/detail/"+ post.slug
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail(subject,message,email_from,recipient_list)
    return redirect('/detail/'+post.slug)
    