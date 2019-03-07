from rest_framework import routers
from django.conf.urls import include,url
from rest_framework.authtoken import views as authview
router=routers.DefaultRouter()
from movie_app.nixapi import views
router.register('nixapi',views.NIXAPI)

urlpatterns = [
    url(r'',include(router.urls)),
    url(r'^get-token/',authview.obtain_auth_token,name='get-token')
]