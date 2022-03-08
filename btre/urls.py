from django.contrib import admin
from django.urls import path, include

import pages

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]
