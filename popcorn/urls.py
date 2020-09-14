
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),


    # local apps urls
    path('', include('pages.urls')),  # main home page url path
    path('account/', include('accounts.urls')),  # accounts
    path('dashboard-x/', include('dashboard.urls'))



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
