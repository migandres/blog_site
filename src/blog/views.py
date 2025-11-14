from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.decorators.http import require_POST 
from django.core.mail import send_mail
from .models import Post
from .forms import EmailPostForm, CommentForm

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

    def paginate_queryset(self, queryset, page_size):
        paginator = Paginator(queryset, page_size)
        page = self.request.GET.get('page')
        return (
            paginator, 
            paginator.get_page(page),
            paginator.get_page(page).object_list,
            paginator.get_page(page).has_other_pages(),
        )

def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})

def post_share(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
            post.get_absolute_url()
            )
            subject = (
            f"{cd['name']} ({cd['email']}) "
            f"Te recomiendo leer: {post.title}"
            )
            message = (
            f"Lee {post.title} a {post_url}\n\n"
            f"{cd['name']}\'s comments: {cd['comments']}"
            )
            send_mail(
            subject=subject,
            message=message,
            from_email=None,
            recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', { 'post': post, 'form': form, 'sent': sent })

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
        Post,
        id = post_id,
        status = Post.Status.PUBLISHED
    )
    comment = None
    form = CommentForm(data = request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request,
        'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment
        }
    )

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
        Post, 
        id=post_id, 
        status=Post.Status.PUBLISHED
    )
    comment = None
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = Comment(
            post=post,
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            body=form.cleaned_data['body']
        )
        comment.save()
    return render(
        request, 
        'blog/post/comment.html', {
        'post': post,
        'form': form,
        'comment': comment
        }
    )