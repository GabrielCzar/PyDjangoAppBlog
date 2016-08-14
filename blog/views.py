from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

#page home
def post_list(request):
	posts_ord_publ_date = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts_ord_publ_date})

def post_detail(request, pk):
    post = get_object_or_404(Post , pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})