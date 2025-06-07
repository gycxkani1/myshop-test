from django.test import TestCase
from .models import GoodsCategory, Goods

# Create your tests here.

class TestGoodModel(TestCase):
    def setUp(self):
        self.good = Goods.objects.create(
            name='测试商品',
            market_price=100.00,
            price=80.00,
            unit='pcs',
            click_num=10,
            amount=5,
            stock_num=20,
            fav_num=2,
            status=0,
            is_recommend=True,
            category_id=1,  # Assuming a category with ID 1 exists
        )
    def test_goodmodel(self):
        good=Goods.objects.get(id=self.good.id)
        self.assertEqual(good.price, 80.00)
