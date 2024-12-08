from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("topic/<slug:name>", views.category_list , name = "category-list"),
     path("thread/<slug:slug>", views.single_post, name="single-post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)