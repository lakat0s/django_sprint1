from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('posts/<int:id>/', include('blog.urls', namespace='blog')),
    path('category/<slug:category_slug>/', include(
        'blog.urls', namespace='blog')),
    path('pages/about/', include('pages.urls', namespace='pages')),
    path('pages/rules/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
]
