from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from jchm.rest import UserViewSet
from jchm.app.rest import (OrgUnitViewSet, LangViewSet, FileViewSet,
                           DocumentViewSet,
                           ModuleViewSet, OrgUnitModuleViewSet)

admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orgunits', OrgUnitViewSet)
router.register(r'langs', LangViewSet)
router.register(r'files', FileViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'orgunitmodules', OrgUnitModuleViewSet)


urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/',
                           include('rest_framework.urls',
                                   namespace='rest_framework'))
                       )

# Development
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = media + staticfiles_urlpatterns() + urlpatterns
