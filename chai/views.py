from django.shortcuts import render
from .models import Blog
from .forms import BlogForm , UserRegistrationForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def all_chai(request):
    return render(request,'chai/all_chai.html')


def blog_list(request):
    blogs =Blog.objects.all().order_by("-created_at")
    return render(request, 'blog_list.html', {'blogs':blogs})


@login_required
def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form=BlogForm()
    return render(request, 'blog_form.html', {'form':form})    


@login_required
def blog_edit(request , blog_id):
    blog= get_object_or_404(Blog, pk=blog_id , author = request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST , request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
        
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form':form})    
    
@login_required    
def blog_del(request, blog_id):
    blog= get_object_or_404(Blog, pk=blog_id , author = request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog_delete.html' , {'blog':blog})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return redirect('blog_list')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html',{'form':form })