from django.shortcuts import render
from django.http import HttpResponse
from Blogging.models import category , post
 
def home(request):
    # request is handled using HttpResponse object
    posts = post.objects.all()
    cats = category.objects.all()
    if request.method=='GET':
        searching = request.GET.get('search')
        if searching!=None:
            posts = post.objects.filter(title=searching)
    data = {
        'post':posts , 
        'cats':cats
    }
    return render(request , 'home.html' , data )

def posts(request , url):
    p = post.objects.get(url=url)
    cats = category.objects.all()
    # print(p)
    return render(request , 'post.html' , {'p':p,'cats':cats})
