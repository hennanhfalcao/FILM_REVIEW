from django.urls import path
from . import views

app_name = 'review'
urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slugify>', views.review_detail, name='review_detail'),
    path('<int:review_id>/add_comment', views.add_comment, name='add_comment'),
]