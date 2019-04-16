from django.shortcuts import render

posts = [
	{
		'author': 'rafa',
		'title': 'blog post1',
		'content': 'first post cont uwu',
		'date_posted': 'August 28, 2018'
	},
	{
		'author': 'fara',
		'title': 'blog post2',
		'content': '2nd post cont uwu',
		'date_posted': 'August 29, 2018'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
