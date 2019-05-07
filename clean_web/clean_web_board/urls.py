from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.Clean_web_board.as_view(), name='clean_web_board'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)