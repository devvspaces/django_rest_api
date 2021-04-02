
from django.contrib import admin
from django.urls import path, include

from postings.api.views import BlogPostRudView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/postings/', include('postings.api.urls')),
]
