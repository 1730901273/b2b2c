# """接下来需要做的就是创建Serializer类，类似于from，
# 它的作用就是从你传入的参数中提取你徐需要的数据，并
# 把它转化为json格式"""
from rest_framework import serializers
from Bills.models import bill


# 它序列化的方法类似于Django的froms
# 创建一个记账API

class getBill(serializers.ModelSerializer):
    class Meta:
        model = bill
        fields = '__all__'
