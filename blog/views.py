from django.shortcuts import render
from django.utils import timezone
from .models import Post
#create your views here

#page home
def post_list(request):
	posts_ord_publ_date = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts_ord_publ_date})
