from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .models import Review, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.http import HttpRequest
from django.views.decorators.http import require_POST
from django.contrib import messages

def review_list(request: HttpRequest):
    reviews = Review.published.all()
    paginator = Paginator(reviews, 1)
    page_number = request.GET.get('page', 1)
    try:
        reviews_page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        reviews_page = paginator.page(1)    
    return render(request, 'review/list.html', {'reviews_page': reviews_page})

def review_detail(request, year, month, day, slugify):
    form = CommentForm()
    review: Review = get_object_or_404(Review.published, published_at__year=year, published_at__month=month, published_at__day=day, slugify=slugify)

    comments = review.comments.filter(active=True)
    return render(request, 'review/detail.html', {'review': review, 'form': form, 'comments': comments})

@require_POST
def add_comment(request, review_id):
    review = get_object_or_404(Review.published, id=review_id)
    form = CommentForm(data=request.POST)
    
    if form.is_valid():
        comment: Comment = form.save(commit = False)
        comment.review = review
        comment.save()
        messages.success(request, 'Your comment has been added successfully.')
        return redirect(review)
    else:
        return render(request, 'review/detail.html', {'review': review, 'form': form})