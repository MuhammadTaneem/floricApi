from users.views import RedirectView, ActiveView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('password/reset/confirm/<uid>/<token>/', RedirectView),
    path('activate/<uid>/<token>/', ActiveView),
    # path('api/profile/', include('users.urls')),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)