from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Seamless_Accounting/', include('Seamless_Accounting.urls', namespace='Seamless_Accounting')),
)
