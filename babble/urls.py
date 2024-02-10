from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('core/', include('core.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
]
