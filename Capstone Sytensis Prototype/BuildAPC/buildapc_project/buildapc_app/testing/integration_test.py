from django.test import TestCase
from django.contrib.auth.models import User
from unittest.mock import patch, MagicMock
from buildapc_app.management.commands.buildapcgo import BuildAPCAdminCLI
from buildapc_app.models import CPU, Cooler, Motherboard, RAM, GPU, Storage, PowerSupply, Tower, OperatingSystem, Monitor

class TestBuildAPCAdminCLIIntegration(TestCase):
    def setUp(self):
        # Create a superuser for testing login functionality
        self.user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
        self.cli = BuildAPCAdminCLI()
        self.cli.stdout = MagicMock()

    def test_login_functionality(self):
        # Test login functionality with correct credentials
        with patch('getpass.getpass', return_value='adminpass'):
            with patch('builtins.input', return_value='admin'):
                self.cli.do_login('')
                self.assertIn('Login successful.', self.cli.stdout.write.call_args_list[0][0][0])

        # Test login functionality with incorrect credentials
        with patch('getpass.getpass', return_value='wrongpass'):
            with patch('builtins.input', return_value='admin'):
                self.cli.do_login('')
                self.assertIn('Login failed.', self.cli.stdout.write.call_args_list[0][0][0])

    def test_main_menu_navigation(self):
        # Simulate user entering the main menu and selecting a component
        with patch('builtins.input', side_effect=['1', 'Q']):  # Select CPU then quit
            self.cli.main_menu()
            self.assertIn('CPU Management', self.cli.stdout.write.call_args_list[0][0][0])

    def test_component_management_flow(self):
        # Test adding a CPU and verifying database interaction
        with patch('builtins.input', side_effect=['1', '100', 'Intel Core i7', 'Intel', '300', 'Q', 'Q']):  # Add CPU flow
            with patch('buildapc_app.management.commands.buildapcgo.BuildAPCAdminCLI.add_generic') as mock_add:
                self.cli.component_menu('cpu')
                mock_add.assert_called_once()

    def test_full_flow_from_login_to_quit(self):
        # Test the full flow from login to adding a component and quitting
        with patch('getpass.getpass', return_value='adminpass'):
            with patch('builtins.input', side_effect=['admin', '1', 'A', '100', 'Intel Core i9', 'Intel', '500', 'Q', 'Q', 'Q']):
                self.cli.cmdloop()
                self.assertIn('CPU added successfully.', self.cli.stdout.write.call_args_list[0][0][0])


