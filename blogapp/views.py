from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditPostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
# def home(request):
#     name = 'PyCread'
#     context = {
#         'name': name
#     }
#     return render(request, 'blogapp/home.html',context)

#Class based view
class HomeView(ListView):
    model = Post
    template_name = 'blogapp/home.html'
    context_object_name = 'posts'

    # def get_context_data(self, **kwargs):
    #     total_posts = Post.objects.count()
    #     context = super().get_context_data(**kwargs)
    #     context["total_posts"] = total_posts
    #     return context
    

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        total_posts = Post.objects.count()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["total_posts"] = total_posts
        return context
    
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogapp/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView,self).get_context_data(*args, **kwargs)
    #  To show the total likes on the post article page
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes() # function created in the models.py file

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["liked"] = liked
        context['total_likes'] = total_likes
        return context

    

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogapp/add_post.html'
    # fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blogapp/update_post.html'
    #fields = '__all__'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blogapp/delete_post.html'
    success_url = reverse_lazy('home') # will redirect to home page after deleting the post

class AddCategoryView(CreateView):
    model = Category
    template_name = 'blogapp/add_category.html'
    fields = '__all__'

#function based views

def CategoryListView(requests):
    cat_menu_list = Category.objects.all()
    
    return render(requests,'blogapp/categories_list.html',{'cat_menu_list' : cat_menu_list})    

def CategoryView(requests,cats):
    category_posts = Post.objects.filter(category__iexact=cats.replace('-', ' '))
    total_posts = Post.objects.filter(category__iexact=cats.replace('-', ' ')).count()
    return render(requests,'blogapp/categories.html',{'cats' : cats.replace('-', ' '),'category_posts' : category_posts, 'total_posts' : total_posts})

def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))

# Add comment views
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blogapp/add_comment.html'
    #success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
    

