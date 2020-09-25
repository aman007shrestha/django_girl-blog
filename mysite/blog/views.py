from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import HttpResponse
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post_object = get_object_or_404(Post, id=pk)
	return render(request, 'blog/post_detail.html', {'post':post_object})


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post.html', {'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.id)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post.html', {'form':form})
	
