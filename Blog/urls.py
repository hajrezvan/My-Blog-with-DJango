from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import view

urlpatterns = [
    path('', view.homePage),
    path('admin/', admin.site.urls),
    path('about/', view.about),
    path('articles/', include('articles.urls')),
    path('account/', include('account.urls'))
]

# دسترسی به فایل هایی که در پوشه asset قرار دارند.
urlpatterns += staticfiles_urlpatterns()
# دسترسی به فایل هایی که در پوشه media قرار دارند.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
