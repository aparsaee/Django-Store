from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mobiles$', views.mobilelistview, name='mobiles'),
    url(r'^mobiles/(?P<slug>\S+)/$',
        views.mobiledetailview, name='mobile-detail'),
    url(r'^brands$', views.brandlistview, name='brands'),
    url(r'^brands/(?P<slug>\S+)/$',
        views.branddetailview, name='brand-detail'),
    url(r'^myboughtlist$', views.myboughtlist, name='myboughtlist'),
]

urlpatterns += [
    url(r'^mobiles/(?P<slug>\S+)/buy$', views.info, name='info'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signup/success$', views.signupsuccess, name='signupsuccess'),
    url(r'^mobiles/(?P<slug>\S+)/buy/pay$', views.pay, name='pay'),
]
