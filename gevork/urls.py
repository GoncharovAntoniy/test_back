
from django.contrib import admin
from django.urls import path
from base_data.views import CardAPIViews
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/baselist/', CardAPIViews.as_view()),
    path('api-auth/baselist/<int:pk>', CardAPIViews.as_view()),
] 

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)