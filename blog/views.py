from django.shortcuts import render

#the '.' means python will look in the same directory for .models
#the 'import Post' is the class that we created in models.py line 5 - 12
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About us'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact us'})