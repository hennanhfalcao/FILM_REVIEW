from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Review.Status.PUBLISHED)
class Review(models.Model):
    
    class Status(models.IntegerChoices):
        DRAFT = (5, 'Draft')
        PUBLISHED = (10, 'Published')
    
    class Rating(models.IntegerChoices):
        BAD = (1, '1 - Bad')
        POOR = (2, '2 - Poor')
        FAIR = (3, '3 - Fair')
        GOOD = (4, '4 - Good')
        EXCELENT = (5, '5 - Excellent')
        EXCEPTIONAL = (6, '6 - Exceptional')


    title = models.CharField(max_length=200)
    slugify = models.SlugField(max_length=200, unique_for_date='published_at')
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices, default=Rating.FAIR)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedManager()
    comments: models.Manager["Comment"]
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("review:review_detail", args=[self.published_at.year, self.published_at.month, self.published_at.day, self.slugify])
    
    def __str__(self) -> str:
        return f"{self.title} - {self.status}"

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    message = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)