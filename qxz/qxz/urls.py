from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from app.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qxz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', admin.site.urls),
   url(r'^index', index), 
   url(r'^echart', echart), 
   url(r'^who', who), 
   url(r'^user', user), 
   url(r'^ps', ps), 
   url(r'^uptime', uptime), 
   url(r'^execute', execute),
   url(r'^$', login),
   url(r'^check', check),
   url(r'^blank', blank),
   url(r'^useradd',useradd),
   url(r'^userdel',userdel),
   url(r'^morris', morris),
   url(r'^flot',flot),
   url(r'^tables',data),
   url(r'^log',log),
   url(r'^ajax',ajax),
   url(r'^forms',forms),
   url(r'^panels',panels),
   url(r'^buttons',buttons),
   url(r'^notifications',notifications),
   url(r'^typography',typography),
   url(r'^icons',icons),
   url(r'^grid',grid),
)
