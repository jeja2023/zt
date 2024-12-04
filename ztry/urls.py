
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from basic_info import views as basic_info_views
urlpatterns = [
    path('home/', basic_info_views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('info/', include('basic_info.urls',)),
    path('', include('login.urls',)),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

