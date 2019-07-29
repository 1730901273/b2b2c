"""b2b2c URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# from b2b2c_app.views import user_fav, userfav_detail, tb_product


from b2b2c_app.views import tb_product, buyer_login, getBills

urlpatterns = [
    path('admin/', admin.site.urls),
    # 在根目录url.py文件中为rest_framework框架的login和logout视图添加url
    # path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # # 添加一个API接口
    # path('user_fav/', user_fav),
    # # 添加一个删除，增加，更新API
    # path('userfav_detail/', userfav_detail),
    # # 添加一个API接口，实现商品数据的交互
    path('tb_product/', tb_product),
    # 添加一个API接口，实在登录界面密码和用户名的认证
    path('buyer_login/', buyer_login),
    # 添加一个记事本的API
    # path('getBills/', getBills),
    # 添加app的url
    url(r'^', include('Bills.urls')),
    url(r'^', include('BLOG.urls')),
]
