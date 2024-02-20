from django.contrib import admin
from django.urls import path, include
from .views import root_route

urlpatterns = [
    path('', root_route),

    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),       
    
    path('api/', include('profiles.urls')),

    path('', include('posts.urls')),

    path('', include('comments.urls')),

    path('', include('likes.urls')),
    
    path('', include('followers.urls')),
]