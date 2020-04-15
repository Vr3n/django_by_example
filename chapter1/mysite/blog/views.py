from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import EmailPostForm, CommentForm
from .models import Post

import pdb
# Create your views here.


# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3)  # 3 posts in each page.
#     page = request.GET.get('page')  # Indicates the current page number.
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results.
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html', {
#         'posts': posts
#     })

class PostListView(ListView):
    """
    List View For Posts - lists all the published posts.
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)

    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == "POST":
        # A comment was posted.
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Creating Comment object but won't save it to database.
            new_comment = comment_form.save(commit=False)

            # assign the current post to the comment.
            new_comment.post = post

            # Save the comment to database.
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {
        'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form
    })


def post_share(request, post_id):
    # pdb.set_trace()
    # Retieve post by id.
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation.
            cleaned_data = form.cleaned_data
            print(cleaned_data['email'])
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cleaned_data['name']} ({cleaned_data['email']} recommends you reading."
            message = f"Read {post.title} at {post_url}\n\n{cleaned_data['name']}\'s comments: {cleaned_data['comments']}"
            send_mail(subject, message, 'admin@myblog.com',
                      [cleaned_data['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {
        'post': post, 'form': form, 'sent': sent
    })
