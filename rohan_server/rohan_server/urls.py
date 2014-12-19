from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rohan_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^Dashboard/', include('dashboard.urls', namespace="dashboard_urls")),
	url(r'^rest_api/', include('rest_api.urls', namespace="rest_api")),
    url(r'^admin/', include(admin.site.urls)),

)
