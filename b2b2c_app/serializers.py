# """接下来需要做的就是创建Serializer类，类似于from，
# 它的作用就是从你传入的参数中提取你徐需要的数据，并
# 把它转化为json格式"""
from rest_framework import serializers
from b2b2c_app.models import TbProduct, TbBuyer, bill


#
#
# # 它序列化的方法类似于Django的froms
# class userfav_serializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     shopping_id = serializers.IntegerField()
#     linenos = serializers.BooleanField(required=False)  # 用于浏览器上显示
#     language = serializers.ChoiceField(choices=language_choices, default="python")
#     style = serializers.ChoiceField(choices=style_choices, default='friendly')
#
#     def update(self, instance, validated_data):
#         """更新和返回一个已经存在的表实例，给出确定的数据"""
#         instance.shopping_id = validated_data.get('shopping_id', instance.shopping_id)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         """创建一个新对象并返回"""
#         return Userfav.objects.create(**validated_data)
#
#
# # 直接关联表，用户收藏
# class userfav_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Userfav
#         # field = {'id', 'shopping_id', 'linenos', 'language', 'style'}
#         fields = '__all__'
#
#
# # 这里关联的是商品表
# class TbProduct_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = TbProduct
#         fields = '__all__'
#
#
# # 创建一个秒杀商品
# class TbSeckillOrder_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = TbSeckillOrder
#         fields = '__all__'


# 创建一个商品的API

# 实现商品API获取所有商品的数据
class product(serializers.ModelSerializer):
    class Meta:
        model = TbProduct
        fields = '__all__'


# 创建一个登录后的界面认证
class user(serializers.ModelSerializer):
    class Meta:
        model = TbBuyer
        fields = '__all__'


# 创建一个记账API
class getBill(serializers.ModelSerializer):
    class Meta:
        model = bill
        fields = '__all__'
