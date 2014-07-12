from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'shotgun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^shotgun_app/', include('shotgun_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
