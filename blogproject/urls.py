from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('tinymce/', include('tinymce.urls')),
    path('blog/', include('blogapp.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('membersapp.urls')),
    path('<int:uid>/', include('membersapp.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)