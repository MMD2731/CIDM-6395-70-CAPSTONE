from django.test import TestCase
from django.contrib.auth.models import User
from unittest.mock import patch, MagicMock
from buildapc_app.management.commands.buildapcgo import BuildAPCAdminCLI
from buildapc_app.models import CPU, GPU, Tower, RAM, Storage, Product

class TestBuildAPCAdminCLIE2E(TestCase):
    def setUp(self):
        # Create a superuser and sample products for testing
        self.user = User.objects.create_superuser('e2euser', 'e2e@example.com', 'e2epass')
        self.product_cpu = Product.objects.create(vendor_sku='1234567890123', name='Sample CPU Product', manufacturer='Intel', item_price=300)
        self.product_gpu = Product.objects.create(vendor_sku='9876543210987', name='Sample GPU Product', manufacturer='NVIDIA', item_price=700)
        self.product_tower = Product.objects.create(vendor_sku='1234509876543', name='Sample Tower Product', manufacturer='Corsair', item_price=200)
        self.product_ram = Product.objects.create(vendor_sku='5678901234567', name='Sample RAM Product', manufacturer='Kingston', item_price=150)
        self.product_storage = Product.objects.create(vendor_sku='7654321098765', name='Sample Storage Product', manufacturer='Seagate', item_price=250)
        self.cli = BuildAPCAdminCLI()
        self.cli.stdout = MagicMock()

    def test_end_to_end_workflow(self):
        # Simulate a full end-to-end workflow from login to adding components and then exiting
        inputs = [
            'e2euser',                  # username
            '1', 'A',                   # select CPU, add action
            '1234567890123', 'Test CPU', 'Intel', '250',  # CPU details
            '2', 'A',                   # select GPU, add action
            '9876543210987', 'Test GPU', 'NVIDIA', '800',  # GPU details
            '3', 'A',                   # select Tower, add action
            '1234509876543', 'Test Tower', 'Corsair', '220',  # Tower details
            '4', 'A',                   # select RAM, add action
            '5678901234567', 'Test RAM', 'Kingston', '160',  # RAM details
            '5', 'A',                   # select Storage, add action
            '7654321098765', 'Test Storage', 'Seagate', '260',  # Storage details
            'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q'  # Exiting the prompts
        ]
        with patch('getpass.getpass', return_value='e2epass'):
            with patch('builtins.input', side_effect=inputs):
                self.cli.cmdloop()

                # Check that all components were added successfully
                self.assertTrue(GPU.objects.filter(name='Test GPU').exists())
                self.assertTrue(Tower.objects.filter(name='Test Tower').exists())
                self.assertTrue(RAM.objects.filter(name='Test RAM').exists())
                self.assertTrue(Storage.objects.filter(name='Test Storage').exists())

                # Check that user was able to exit
                self.assertIn('Exiting the program.', self.cli.stdout.write.call_args_list[-1][0][0])

    def test_failed_login_and_exit(self):
        # Test the login failure and immediate exit
        with patch('getpass.getpass', return_value='wrongpass'):
            with patch('builtins.input', side_effect=['e2euser', 'Q']):
                self.cli.cmdloop()
                self.assertIn('Login failed.', self.cli.stdout.write.call_args_list[0][0][0])
                self.assertIn('Thank you for using BuildAPC Admin Console.', self.cli.stdout.write.call_args_list[-1][0][0])

