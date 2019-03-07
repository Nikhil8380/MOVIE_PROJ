from . import views
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url(r'^home$', views.LIST.as_view(), name='list'),
    url(r'^$', views.home, name='home'),

    url(r'^register/$', views.Register, name='register'),
    #url(r'^login/$', views.Login, name='login2'),
    #url(r'^logout/$', views.LOGOUT, name='logout2'),
    url(r'^post/(?P<pk>\d+)$', views.DETAIL.as_view(), name='detail'),
    url(r'^post/new/$', views.Create, name='create'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.Update.as_view(), name='update'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.DELETE.as_view(), name='post_remove'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
