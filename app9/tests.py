from django.test import TestCase
from .models import GoodsCategory, Goods

# Create your tests here.
class TestGoodModel(TestCase):
    def setUp(self):
        # 创建测试类别
        self.category = GoodsCategory.objects.create(name='测试分类', sort=1)

    def test_goods_creation(self):
        # 创建商品项
        goods = Goods.objects.create(
            name='测试商品',
            category=self.category,
            market_price=100.00,
            price=80.00
        )
        
        # 检查商品项是否成功创建
        self.assertEqual(goods.name, '测试商品')
        self.assertEqual(goods.category, self.category)
        self.assertEqual(goods.market_price, 100.00)
        self.assertEqual(goods.price, 80.00)

    