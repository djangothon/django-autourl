from django.conf.urls import include, url
from views import home,details,getMeta
from ubuild import log

urlpatterns = [
    url(r'^details/(?P<url>[\w|\W]+)/',details),
    url(r'^metadata/(?P<pk>\d+)/',getMeta),
    url(r'^home/',log(home), name="home"),
    #url(r'^create/',log(create))
]

