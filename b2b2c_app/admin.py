from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from b2b2c_app.models import TbAddress, TbBuyer, TbCategory, TbOrders, TbProduct, TbSeller, TbLogistics, TbOrdersitem, \
    TbProductcar, TbShopcar, TbStore

admin.site.register(TbAddress)
admin.site.register(TbBuyer)
admin.site.register(TbCategory)
admin.site.register(TbLogistics)
# admin.site.register(TbOrdersitem)
admin.site.register(TbProduct)
admin.site.register(TbSeller)
admin.site.register(TbOrders)

admin.site.register(TbShopcar)
admin.site.register(TbStore)


admin.site.site_header = '5+2商城管理平台'
admin.site.site_title = '5+2商城管理平台'


class AreaAdmin(admin.ModelAdmin):
    list_per_page = 10  # 默认显示100
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 定义列表中要显示哪些字段
    search_fields = ['b_id', 'b_username']
    # 表单中字段显示的顺序
    fields = ['b_id', 'b_username']


class TbBuyer(ModelAdmin):
    # 定义列表中要显示哪些字段
    list_display = ['b_id', 'b_username']
