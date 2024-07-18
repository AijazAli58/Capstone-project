from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        # Create an instance of Menu
        menu = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # Test the get_item method
        self.assertEqual(menu.get_item(), "IceCream : 80")
