from rest_framework import serializers
from .models import *

class GoodsCategorySerializer(serializers.Serializer): # 商品分类序列化类
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()

class GoodsSerializer(serializers.Serializer): # 商品序列化类
    name=serializers.CharField(required=True,max_length=100)
    category=serializers.CharField(required=False)#GoodsCategorySerializer()
    #category = GoodsCategorySerializer(required=False,read_only=True) # 序列化嵌套
    market_price =serializers.DecimalField(max_digits=8, decimal_places=2)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    #post_category = serializers.IntegerField(write_only=True)

    def create(self, validated_data): # 对应POST请求，相当于新增数据
        print(type(validated_data),validated_data)
        #validated_data['category_id']=validated_data.get('post_category')
        #goods_obj = Goods.objects.create(
        #    name=validated_data.get('name'),
        #    market_price=validated_data.get('market_price'),
        #    price=validated_data.get('price'),
        #    category_id=validated_data.get('post_category'),
        #)
        return Goods.objects.create(**validated_data)
    
    def update(self, instance,validated_data): # 对应PUT请求，相当于更新数据
        print(type(validated_data),validated_data)
        instance.name=validated_data.get("name")
        instance.market_price=validated_data.get("market_price")
        instance.price=validated_data.get("price")
        instance.save()
        return instance

class GoodsCategoryModelSerializer(serializers.ModelSerializer): # 商品分类模型序列化类
    class Meta:
        model=GoodsCategory
        fields="__all__"

class GoodsModelSerializer(serializers.ModelSerializer): # 商品模型序列化类
    #category=serializers.CharField()
    category=GoodsCategoryModelSerializer()  # 序列化嵌套
    class Meta:
        model=Goods
        fields="__all__"
        #fields=('id','name','category','market_price','price')
