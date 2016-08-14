from django.shortcuts import render

#create your views here

#page home
def post_list(request):
	return render(request, 'blog/post_list.html', {})
