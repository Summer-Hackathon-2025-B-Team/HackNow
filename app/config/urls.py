from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('apps.user.urls')),
    path('home/', include('apps.home.urls')),
    path('course/', include('apps.course.urls')),
    path('team/', include('apps.team.urls')),
    path('past/', include('apps.past.urls')),
    path('task/',include('apps.task.urls')),
    path('meeting/',include('apps.meeting.urls')),
    path('knowledge/', include('apps.knowledge.urls')),
    path('document/', include('apps.document.urls')),
]

# staticディレクトリを参照するための定義
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
