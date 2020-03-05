from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs' : blogs})

def new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('home')        
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form':form})