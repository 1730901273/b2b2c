from django.conf.urls import url
from BLOG.views import *

urlpatterns = [
    url(r'^blog/$', get_blogs),
    url(r'^detail/(\d+)/$', get_details, name='blog_get_detail'),
]
