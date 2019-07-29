# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TbAddress(models.Model):
    a_id = models.AutoField(db_column='A_id', primary_key=True, verbose_name="ID")  # Field name made lowercase.
    a_address = models.CharField(db_column='A_address', max_length=50, verbose_name="地址")  # Field name made lowercase.
    b_foreign = models.ForeignKey('TbBuyer', models.DO_NOTHING, db_column='B_foreign',
                                  verbose_name="买家")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.a_address

    class Meta:
        verbose_name = "收货地址"
        managed = False
        db_table = 'tb_address'


class TbAdmin(models.Model):
    ad_id = models.AutoField(db_column='Ad_id', primary_key=True)  # Field name made lowercase.
    ad_username = models.CharField(db_column='Ad_username', max_length=20)  # Field name made lowercase.
    ad_password = models.CharField(db_column='Ad_password', max_length=20)  # Field name made lowercase.
    ad_nickname = models.CharField(db_column='Ad_nickname', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_admin'


class TbBuyer(models.Model):
    b_id = models.AutoField(db_column='B_id', primary_key=True, verbose_name="买家ID")  # Field name made lowercase.
    username = models.CharField(db_column='B_username', unique=True, max_length=20,
                                  verbose_name="用户名")  # Field name made lowercase.
    password = models.CharField(db_column='B_password', max_length=20,
                                  verbose_name="密码")  # Field name made lowercase.
    b_phone = models.CharField(db_column='B_phone', max_length=15, blank=True, null=True,
                               verbose_name="手机号")  # Field name made lowercase.
    b_nickname = models.CharField(db_column='B_nickname', max_length=20, blank=True, null=True,
                                  verbose_name="昵称")  # Field name made lowercase.
    b_createtime = models.DateTimeField(db_column='B_createtime', verbose_name="注册时间")  # Field name made lowercase.
    b_headportrait = models.CharField(db_column='B_headportrait', max_length=50, blank=True, null=True,
                                      verbose_name="买家头像相对路径")  # Field name made lowercase.
    b_intro = models.CharField(db_column='B_intro', max_length=500, blank=True, null=True,
                               verbose_name="买家简介")  # Field name made lowercase.
    b_taken = models.CharField(db_column='B_taken', max_length=200, null=False, verbose_name="登录taken")  # 记录登录信息taken值

    # 重写方法
    def __str__(self):
        return self.b_nickname

    class Meta:
        verbose_name = "买家表"
        managed = False
        db_table = 'tb_buyer'


class TbCategory(models.Model):
    c_id = models.IntegerField(db_column='C_id', primary_key=True, verbose_name="分类ID")  # Field name made lowercase.
    c_name = models.CharField(db_column='C_name', max_length=20, verbose_name="分类名称")  # Field name made lowercase.
    c_desc = models.CharField(db_column='C_desc', max_length=100, blank=True, null=True,
                              verbose_name="分类描述")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.c_name

    class Meta:
        verbose_name = "分类表"
        managed = False
        db_table = 'tb_category'


class TbLogistics(models.Model):
    l_id = models.AutoField(db_column='L_id', primary_key=True, verbose_name="物流信息ID")  # Field name made lowercase.
    l_start = models.CharField(db_column='L_start', max_length=50, verbose_name="发货地址")  # Field name made lowercase.
    l_current = models.CharField(db_column='L_current', max_length=50,
                                 verbose_name="当前位置")  # Field name made lowercase.
    l_end = models.CharField(db_column='L_end', max_length=50, verbose_name="收货地址")  # Field name made lowercase.
    o_id = models.IntegerField(db_column='O_id', verbose_name="订单ID")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.l_current

    class Meta:
        verbose_name = "物流信息表"
        managed = False
        db_table = 'tb_logistics'


class TbOrders(models.Model):
    o_id = models.AutoField(db_column='O_id', primary_key=True, verbose_name="订单ID")  # Field name made lowercase.
    o_bname = models.CharField(db_column='O_bname', max_length=20, verbose_name="收货人姓名")  # Field name made lowercase.
    o_bphone = models.CharField(db_column='O_bphone', max_length=15, verbose_name="收货人电话")  # Field name made lowercase.
    o_time = models.DateTimeField(db_column='O_time', verbose_name="订单生成时间")  # Field name made lowercase.
    o_address = models.CharField(db_column='O_address', max_length=100,
                                 verbose_name="收货地址")  # Field name made lowercase.
    o_state = models.IntegerField(db_column='O_state', verbose_name="订单状态 ")  # Field name made lowercase.
    o_total = models.FloatField(db_column='O_total', blank=True, null=True,
                                verbose_name="订单总价")  # Field name made lowercase.
    b_no = models.ForeignKey(TbBuyer, models.DO_NOTHING, db_column='B_no',
                             verbose_name="买家ID")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.o_bname

    class Meta:
        verbose_name = "订单表"
        managed = False
        db_table = 'tb_orders'


class TbOrdersitem(models.Model):
    p_no = models.ForeignKey('TbProduct', models.DO_NOTHING, db_column='P_no',
                             verbose_name="商品ID")  # Field name made lowercase.
    o_no = models.ForeignKey(TbOrders, models.DO_NOTHING, db_column='O_no',
                             verbose_name="订单ID")  # Field name made lowercase.
    oi_count = models.IntegerField(db_column='OI_count', verbose_name="商品数量")  # Field name made lowercase.
    oi_sum = models.FloatField(db_column='OI_sum', verbose_name="小计金额")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.o_no

    class Meta:
        verbose_name = "订单项表"
        managed = False
        db_table = 'tb_ordersitem'


class TbProduct(models.Model):
    p_id = models.AutoField(db_column='P_id', primary_key=True, verbose_name="商品ID")  # Field name made lowercase.
    p_name = models.CharField(db_column='P_name', max_length=50, verbose_name="商品名")  # Field name made lowercase.
    p_price = models.FloatField(db_column='P_price', verbose_name="商品单价")  # Field name made lowercase.
    p_uptime = models.DateTimeField(db_column='P_uptime', verbose_name="商品上架时间")  # Field name made lowercase.
    p_image = models.CharField(db_column='P_image', max_length=50,
                               verbose_name="商品图片相对路径地址")  # Field name made lowercase.
    p_desc = models.CharField(db_column='P_desc', max_length=500, blank=True, null=True,
                              verbose_name="商品描述")  # Field name made lowercase.
    p_inventory = models.IntegerField(db_column='P_inventory', blank=True, null=True,
                                      verbose_name="商品库存量")  # Field name made lowercase.
    c_no = models.ForeignKey(TbCategory, models.DO_NOTHING, db_column='C_no',
                             verbose_name="分类ID")  # Field name made lowercase.
    st_no = models.ForeignKey('TbSeller', models.DO_NOTHING, db_column='St_no',
                              verbose_name="店铺ID")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.p_name

    class Meta:
        verbose_name = "商品表"
        managed = False
        db_table = 'tb_product'


class TbProductcar(models.Model):
    sc_no = models.ForeignKey('TbShopcar', models.DO_NOTHING, db_column='Sc_no', blank=True, null=True,
                              verbose_name="购物车ID")  # Field name made lowercase.
    p_no = models.ForeignKey(TbProduct, models.DO_NOTHING, db_column='P_no', blank=True, null=True,
                             verbose_name="商品ID")  # Field name made lowercase.
    pc_state = models.IntegerField(db_column='Pc_state', blank=True, null=True,
                                   verbose_name="交易状态")  # Field name made lowercase.
    pc_count = models.IntegerField(db_column='Pc_count', blank=True, null=True,
                                   verbose_name="商品数量")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.pc_state

    class Meta:
        verbose_name = "购物车商品表"
        managed = False
        db_table = 'tb_productcar'


class TbSeller(models.Model):
    s_id = models.AutoField(db_column='S_id', primary_key=True, verbose_name="卖家ID")  # Field name made lowercase.
    s_username = models.CharField(db_column='S_username', unique=True, max_length=20,
                                  verbose_name="用户名")  # Field name made lowercase.
    s_password = models.CharField(db_column='S_password', max_length=20,
                                  verbose_name="密码")  # Field name made lowercase.
    s_phone = models.CharField(db_column='S_phone', max_length=15, blank=True, null=True,
                               verbose_name="手机号")  # Field name made lowercase.
    s_nickname = models.CharField(db_column='S_nickname', max_length=20, blank=True, null=True,
                                  verbose_name="昵称")  # Field name made lowercase.
    s_createtime = models.DateTimeField(db_column='S_createtime', verbose_name="注册时间")  # Field name made lowercase.
    s_headportrait = models.CharField(db_column='S_headportrait', max_length=50, blank=True, null=True,
                                      verbose_name="卖家头像相对路径")  # Field name made lowercase.
    s_intro = models.CharField(db_column='S_intro', max_length=500, blank=True, null=True,
                               verbose_name="卖家简介")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.s_nickname

    class Meta:
        verbose_name = "卖家个人信息表 "
        managed = False
        db_table = 'tb_seller'


class TbShopcar(models.Model):
    sc_id = models.AutoField(db_column='Sc_id', primary_key=True, verbose_name="购物车ID")  # Field name made lowercase.
    b_no = models.IntegerField(db_column='B_no', unique=True, verbose_name="商品ID")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.b_no

    class Meta:
        verbose_name = "购物车表"
        managed = False
        db_table = 'tb_shopcar'


class TbStore(models.Model):
    st_id = models.AutoField(db_column='St_id', primary_key=True, verbose_name="店铺ID")  # Field name made lowercase.
    st_name = models.CharField(db_column='St_name', unique=True, max_length=20,
                               verbose_name="店铺名称")  # Field name made lowercase.
    st_desc = models.CharField(db_column='St_desc', max_length=500, blank=True, null=True,
                               verbose_name="店铺描述")  # Field name made lowercase.
    s_id = models.IntegerField(db_column='S_id', verbose_name="卖家ID")  # Field name made lowercase.

    # 重写方法
    def __str__(self):
        return self.st_name

    class Meta:
        verbose_name = "店铺表"
        managed = False
        db_table = 'tb_store'


# 创建记账本数据表
class bill(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, verbose_name="记账本id")
    time = models.DateTimeField(db_column='time', verbose_name="记账时间")
    amount = models.IntegerField(db_column="amount", verbose_name="金额(分)")
    memo = models.CharField(db_column="memo", max_length=100, verbose_name="备注")

    # 重写方法
    def __str__(self):
        return str(self.memo)

    class Meta:
        verbose_name = "记账表"
        managed = False
        db_table = 'bill'

