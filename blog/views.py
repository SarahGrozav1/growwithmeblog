from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, CollaborateForm
from .forms import CommentForm
from .forms import CollaborateRequestForm
from django.contrib.auth.mixins import LoginRequiredMixin


# class HomeScreen(LoginRequiredMixin, generic.ListView):
#     login_url = '/'
#     model = Post
#     template_name = 'index.html'

class HomeScreen(View):

    def get(self, request):
        if request.user.is_authenticated:

            return redirect(
                '/dashboard'               
            )
        else:
             return render(
                request,
                "index.html",
            )



class Dashboard(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = Post
    template_name = 'dashboard.html'
    


class ConclusionScreen(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'conclusion.html'
    paginate_by = 1

class BooksScreen(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'books.html'
    paginate_by = 6

class ParentingScreen(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'parenting.html'
    paginate_by = 6

class FashionScreen(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'parenting.html'
    paginate_by = 6


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'skincare.html'
    paginate_by = 6



class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def Collaboration(request):
    """
    Renders the Collaboration page
    """
    
    collaborate_form = CollaborateRequestForm()

    return render(
        request,
        "collaboration.html",
        {
            
            "collaborate_form": collaborate_form
        },
    )


def about_me(request):
    """
    Renders the About page
    """
    return render(
        request,
        "about.html",
    )