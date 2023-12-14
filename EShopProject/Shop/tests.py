from django.test import TestCase
from django.urls import reverse, resolve
from .views import allproducts, prod_det

class TestURL(TestCase):
  def test_urlallproducts(self):
    url=reverse('product_by_category', args=['demo_slug'])
    print("url is :", url)
    print("Resolve :", resolve(url))
    self.assertEqual(resolve(url).func, allproducts)

  def test_urlprodcat(self):
    url=reverse('product_catdetail', args=['demo_slug','demo_slug2'])
    print("url is :", url)
    print("Resolve :", resolve(url))
    self.assertEqual(resolve(url).func, prod_det)

# Create your tests here.
