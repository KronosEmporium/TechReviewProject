from django.test import TestCase
from TechReviewApp.models import Product, TechType, Review
from TechReviewApp.views import index, gettypes, getproducts
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class TechTypeTest(TestCase):
    def test_string(self):
        type = TechType(techtypename = "Tablet")
        self.assertEqual(str(type), type.techtypename)

    def test_table(self):
        self.assertEqual(str( TechType._meta.db_table), 'techtype')

class ProductTest(TestCase):
    def setup(self):
        type = TechType(techtypename = "laptop")
        product = Product(productname = "Lenovo", techtype = type, productprice = "500.00")
        return product

    def test_string(self):
        prod = self.setup()
        self.assertEqual(str(prod), prod.productname)

    def test_discount(self):
        prod = self.setup()
        self.assertEqual(prod.memberDiscount(), 25.00)

    def test_type(self):
        prod = self.setup()
        self.assertEqual(str(prod.techtype), "laptop")

    def test_table(self):
        self.assertEqual(str(Product._meta.db_table), 'product')

class ReviewTest(TestCase):
    def test_string(self):
        rev = Review(reviewtitle = "Best Review")
        self.assertEqual(str(rev), rev.reviewtitle)

    def test_table(self):
        self.assertEqual(str(Review._meta.db_table), 'review')

class IndexTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)

    def setup(self):
        u = User.objects.create(username = 'myuser')
        type = TechType.objects.create(techtypename = 'laptop')
        prod = Product.objects.create(productname = 'product1', techtype = type, user = u, productprice = 500, productentrydate = '2019-04-02', productdescription = "a product")
        rev1 = Review.objects.create(reviewtitle = 'prodreview', reviewdate = '2019-04-03', product = prod, rating = 4, reviewtext = 'some review')
        rev1.user.add(u)
        rev2 = Review.objects.create(reviewtitle= 'prodreview', reviewdate = '2019-04-03', product = prod, rating = 4, reviewtext = 'some review')
        rev2.user.add(u)
        return prod
    
    def test_product_detail_success(self):
        deets = self.setup()
        response = self.client.get(reverse("productdetails", args = (deets.id,)))
        self.assertEqual(response.status_code, 200)