from django.conf.urls import include, url
from django.contrib import admin

from views import HomeView

urlpatterns = [
    # Examples:
    # url(r'^$', 'cache_property.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
