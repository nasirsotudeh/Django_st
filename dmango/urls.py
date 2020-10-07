
from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include , url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
