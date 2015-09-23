from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demohse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'vistasdemo.views.perfiles'),
    url(r'^perfiles/$', 'vistasdemo.views.perfiles'),
    url(r'^contratista/$', 'vistasdemo.views.contratista'),
    url(r'^actividades/$', 'vistasdemo.views.actividades'),
    url(r'^documentosrequeridos/$', 'vistasdemo.views.documentosrequeridos'),
    url(r'^cuadrilla/$', 'vistasdemo.views.cuadrilla'),
    url(r'^areas/$', 'vistasdemo.views.areas'),
    url(r'^permisostrabajo/$', 'vistasdemo.views.permisostrabajo'),
    url(r'^contratante/$', 'vistasdemo.views.contratante'),
)




urlpatterns += staticfiles_urlpatterns()
