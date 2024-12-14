from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.http import Http404
from . import views


urlpatterns = [
     path("", views.index, name="index"),
     path("topic/<slug:slug>", views.category_list , name = "category-list"),
     path("article/<slug:slug>", views.single_post, name="single-post"),
     path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit-comment'),
     path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete-comment'),
     path('comment/<int:comment_id>/upvote/', views.upvote_comment, name='upvote_comment'),
     path('comment/<int:comment_id>/downvote/', views.downvote_comment, name='downvote_comment'),
     path('test-404/', lambda request: (_ for _ in ()).throw(Http404)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)