from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# sa rozne mozliwosci tak zwanych class base views
# sa ListView, DetailView, CreateView, UpdateView, DeleteView
# wszystkie sa z modulu django.views.generic


def home(request):
	contex = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', contex)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_post.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post
	# pk_url_kwarg = 'author'


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title', 'content']
	# success_url = '/' moglbym tego uzyc jakbym chcial miec redirect do bloga
	# pk_url_kwarg = 'author'
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title', 'content']
	# success_url = '/' moglbym tego uzyc jakbym chcial miec redirect do bloga
	# pk_url_kwarg = 'author'
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	# pk_url_kwarg = 'author'
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

# class CreateComment(CreateView):
# 	model = Comment
# 	template_name = 'create_comment.html'

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})


	