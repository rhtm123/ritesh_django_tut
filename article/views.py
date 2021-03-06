from django.shortcuts import render, HttpResponse

from article.models import Blog

# Create your views here.

def home(request):
	return HttpResponse("Home PAGE")

def about(request):
	return render(request, 'about.html')

def contact(request):
	return HttpResponse("CONTACT PAGE")

def all_blogs(request):
	blogs = Blog.objects.all()

	context_dict = {'blogs':blogs,'name':"ritesh","key":"value"}

	return render(request, 'blogs.html', context_dict)