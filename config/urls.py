# from django.contrib import admin
# from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns=[path('admin/',admin.site.urls),path('api/auth/',include('rest_framework.urls')),path('api/',include('core.urls'))]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # API authentication: obtain a token using username and password
    path('api/auth/', obtain_auth_token, name='api-auth'),

    # EcoSphere application API endpoints
    path('api/', include('core.urls')),
]


# Serve uploaded media files during local development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
