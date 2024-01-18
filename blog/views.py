from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, CollaborateRequest, Comment
from .forms import CommentForm
from .forms import CollaborateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# If user is authenticated to redirect him to dashboard else to stay in index
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

# LoginRequiredMixin is to verifie if user is authenticated
class Dashboard(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = Post
    template_name = 'dashboard.html'
    
# Conclusion Page
class ConclusionScreen(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'conclusion.html'
    paginate_by = 1

# Category tells me the id of the categorie I want for this class witch is books
class BooksScreen(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, category=2).order_by('-created_on')
    template_name = 'books.html'
    paginate_by = 6

# AN EXAMPLE OF A FUNCTION - IT WILL GIVE ME THE SAME AS THE ONE WITH THE CLASS FOR BOOKS
# def BooksScreen(request):
#     post = Post.objects.filter(category=2)

#     return render(
#         request, 
#         'books.html', 
#         {
#             "post_list": post
#         }
#     )

class FashionScreen(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, category=3).order_by('-created_on')
    template_name = 'fashion.html'
    paginate_by = 6

class SkincareScreen(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, category=4).order_by('-created_on')
    template_name = 'skincare.html'
    paginate_by = 6

class ParentingScreen(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, category=5).order_by('-created_on')
    template_name = 'parenting.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")
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
        
        return HttpResponseRedirect(reverse('blog:post_detail', args=[slug]))
    
# Function for edit button
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.email == request.user.email:
            comment = comment_form.save(commit=False)
            comment.post = post
            
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('blog:post_detail', args=[slug]))

# Function for delete button
def comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """

    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.email == request.user.email:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment Deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('blog:post_detail', args=[slug]))


def Collaboration(request):
    """
    Renders the Collaboration page
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I will respond within 3 working days.")
            return HttpResponseRedirect(reverse('blog:collaboration'))
    else:
        collaborate_form = CollaborateForm()

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
