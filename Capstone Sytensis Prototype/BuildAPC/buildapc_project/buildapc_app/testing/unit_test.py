from django.test import TestCase
from unittest.mock import patch, MagicMock
from django.contrib.auth.models import User
from buildapc_app.management.commands.buildapcgo import BuildAPCAdminCLI
from buildapc_app.models import Cooler, Motherboard, RAM, GPU, Storage, PowerSupply, Tower, OperatingSystem, Monitor

class TestBuildAPCAdminCLIUnit(TestCase):
    def setUp(self):
        # Setup a test user and command line interface instance
        self.user = User.objects.create_user(username='testuser', password='password')
        self.cli = BuildAPCAdminCLI()
        self.cli.stdout = MagicMock()

    def test_do_login_successful(self):
        # Test successful login
        with patch('getpass.getpass', return_value='password'):
            with patch('builtins.input', return_value='testuser'):
                self.assertTrue(self.cli.do_login(''))

    def test_do_login_failed(self):
        # Test failed login due to incorrect password
        with patch('getpass.getpass', return_value='wrongpassword'):
            with patch('builtins.input', return_value='testuser'):
                self.assertTrue(self.cli.do_login(''))

    def test_do_quit(self):
        # Test quitting the application
        self.assertTrue(self.cli.do_quit(''))

    @patch('builtins.input', side_effect=['Q'])
    def test_main_menu_quit(self, mocked_input):
        # Test quitting from the main menu
        self.cli.main_menu()
        self.cli.stdout.write.assert_called_with('Exiting the program.')

    @patch('builtins.input', side_effect=['1', 'Q'])  # Select CPU management then quit
    def test_main_menu_cpu_management(self, mocked_input):
        self.cli.main_menu()
        self.cli.stdout.write.assert_called_with('Invalid choice, try again.')

    @patch('builtins.input', side_effect=['A', 'Q'])  # Select Add operation then quit
    def test_component_menu_add(self, mocked_input):
        self.cli.component_menu('CPU')
        self.cli.stdout.write.assert_called_with('Invalid action, try again.')

    def test_add_generic(self):
        # Assuming add_generic is correctly implemented
        with patch('buildapc_app.management.commands.buildapcgo.BuildAPCAdminCLI.add_generic', return_value=None) as mocked_add:
            mocked_add('CPU')
            mocked_add.assert_called_once()

    def test_edit_generic(self):
        # Test editing functionality
        with patch('buildapc_app.management.commands.buildapcgo.BuildAPCAdminCLI.edit_generic', return_value=None) as mocked_edit:
            mocked_edit('CPU')
            mocked_edit.assert_called_once()

    def test_view_generic(self):
        # Test viewing functionality
        with patch('buildapc_app.management.commands.buildapcgo.BuildAPCAdminCLI.view_generic', return_value=None) as mocked_view:
            mocked_view('CPU')
            mocked_view.assert_called_once()

    def test_delete_generic(self):
        # Test delete functionality
        with patch('buildapc_app.management.commands.buildapcgo.BuildAPCAdminCLI.delete_generic', return_value=None) as mocked_delete:
            mocked_delete('CPU')
            mocked_delete.assert_called_once()

    # Cooler Tests
    @patch('builtins.input', side_effect=['1', 'New Cooler', 'BeCool', '150'])
    def test_add_cooler(self, mock_input):
        with patch.object(self.cli, 'add_generic', return_value=None) as mocked_add:
            self.cli.a_cooler()
            mocked_add.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_delete_cooler(self, mock_input):
        with patch.object(self.cli, 'delete_generic', return_value=None) as mocked_delete:
            self.cli.d_cooler()
            mocked_delete.assert_called_once_with(Cooler, 1)

    @patch('builtins.input', side_effect=['1', 'Updated Cooler', 'Frozen', '250'])
    def test_edit_cooler(self, mock_input):
        with patch.object(self.cli, 'edit_generic', return_value=None) as mocked_edit:
            self.cli.e_cooler()
            mocked_edit.assert_called_once()

    def test_view_coolers(self):
        with patch.object(self.cli, 'view_generic', return_value=None) as mocked_view:
            self.cli.v_cooler()
            mocked_view.assert_called_once_with(Cooler)

# Motherboard Tests
    @patch('builtins.input', side_effect=['1', 'ASUS ROG', 'MSI', '350'])
    def test_add_motherboard(self, mock_input):
        with patch.object(self.cli, 'add_generic', return_value=None) as mocked_add:
            self.cli.a_motherboard()
            mocked_add.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_delete_motherboard(self, mock_input):
        with patch.object(self.cli, 'delete_generic', return_value=None) as mocked_delete:
            self.cli.d_motherboard()
            mocked_delete.assert_called_once_with(Motherboard, 1)

    @patch('builtins.input', side_effect=['1', 'Updated Motherboard', 'NZXT', '400'])
    def test_edit_motherboard(self, mock_input):
        with patch.object(self.cli, 'edit_generic', return_value=None) as mocked_edit:
            self.cli.e_motherboard()
            mocked_edit.assert_called_once()

    def test_view_motherboards(self):
        with patch.object(self.cli, 'view_generic', return_value=None) as mocked_view:
            self.cli.v_motherboard()
            mocked_view.assert_called_once_with(Motherboard)

    # RAM Tests
    @patch('builtins.input', side_effect=['1', 'Corsair Vengeance', 'GForce', '500'])
    def test_add_ram(self, mock_input):
        with patch.object(self.cli, 'add_generic', return_value=None) as mocked_add:
            self.cli.a_ram()
            mocked_add.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_delete_ram(self, mock_input):
        with patch.object(self.cli, 'delete_generic', return_value=None) as mocked_delete:
            self.cli.d_ram()
            mocked_delete.assert_called_once_with(RAM, 1)

    @patch('builtins.input', side_effect=['1', 'Updated RAM', 'SpeedMe', '550'])
    def test_edit_ram(self, mock_input):
        with patch.object(self.cli, 'edit_generic', return_value=None) as mocked_edit:
            self.cli.e_ram()
            mocked_edit.assert_called_once()

    def test_view_rams(self):
        with patch.object(self.cli, 'view_generic', return_value=None) as mocked_view:
            self.cli.v_ram()
            mocked_view.assert_called_once_with(RAM)

    # GPU Tests
    @patch('builtins.input', side_effect=['1', 'GeForce RTX 3080', 'nVIDIA', '1500'])
    def test_add_gpu(self, mock_input):
        with patch.object(self.cli, 'add_generic', return_value=None) as mocked_add:
            self.cli.a_gpu()
            mocked_add.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_delete_gpu(self, mock_input):
        with patch.object(self.cli, 'delete_generic', return_value=None) as mocked_delete:
            self.cli.d_gpu()
            mocked_delete.assert_called_once_with(GPU, 1)

    @patch('builtins.input', side_effect=['1', 'Updated GPU', 'AMD', '2300'])
    def test_edit_gpu(self, mock_input):
        with patch.object(self.cli, 'edit_generic', return_value=None) as mocked_edit:
            self.cli.e_gpu()
            mocked_edit.assert_called_once()

    def test_view_gpus(self):
        with patch.object(self.cli, 'view_generic', return_value=None) as mocked_view:
            self.cli.v_gpu()
            mocked_view.assert_called_once_with(GPU)

# Storage Tests
    @patch('builtins.input', side_effect=['1', 'Seagate Expansion', 'Western Digital', '850'])
    def test_add_storage(self, mock_input):
        with patch.object(self.cli, 'add_generic', return_value=None) as mocked_add:
            self.cli.a_storage()
            mocked_add.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_delete_storage(self, mock_input):
        with patch.object(self.cli, 'delete_generic', return_value=None) as mocked_delete:
            self.cli.d_storage()
            mocked_delete.assert_called_once_with(Storage, 1)

    @patch('builtins.input', side_effect=['1', 'Updated Storage', 'Lucie', '900'])
    def test_edit_storage(self, mock_input):
        with patch.object(self.cli, 'edit_generic', return_value=None) as mocked_edit:
            self.cli.e_storage()
            mocked_edit.assert_called_once()

    def test_view_storage(self):
        with patch.object(self.cli, 'view_generic', return_value=None) as mocked_view:
            self.cli.v_storage()
            mocked_view.assert_called_once_with(Storage)

    # PowerSupply Tests
    @patch('builtins.input', side_effect=['1', 'SuperNova', 'ChargeUp', '450'])
    def test_add_powersupply(self, mock_input):
        with patch.object(self.cli, 'add_generic', return_value=None) as mocked_add:
            self.cli.a_powersupply()
            mocked_add.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_delete_powersupply(self, mock_input):
        with patch.object(self.cli, 'delete_generic', return_value=None) as mocked_delete:
            self.cli.d_powersupply()
            mocked_delete.assert_called_once_with(PowerSupply, 1)

    @patch('builtins.input', side_effect=['1', 'Updated PowerSupply', 'NxtLVLEnergy', '500'])
    def test_edit_powersupply(self, mock_input):
        with patch.object(self.cli, 'edit_generic', return_value=None) as mocked_edit:
            self.cli.e_powersupply()
            mocked_edit.assert_called_once()

    def test_view_powersupply(self):
        with patch.object(self.cli, 'view_generic', return_value=None) as mocked_view:
            self.cli.v_powersupply()
            mocked_view.assert_called_once_with(PowerSupply)

    # Tower Tests
    @patch('builtins.input', side_effect=['1', 'Corsair Case', 'NZXT', '200'])
    def test_add_tower(self, mock_input):
        with patch.object(self.cli, 'add_generic', return_value=None) as mocked_add:
            self.cli.a_tower()
            mocked_add.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_delete_tower(self, mock_input):
        with patch.object(self.cli, 'delete_generic', return_value=None) as mocked_delete:
            self.cli.d_tower()
            mocked_delete.assert_called_once_with(Tower, 1)

    @patch('builtins.input', side_effect=['1', 'Updated Tower', 'Xteam', '250'])
    def test_edit_tower(self, mock_input):
        with patch.object(self.cli, 'edit_generic', return_value=None) as mocked_edit:
            self.cli.e_tower()
            mocked_edit.assert_called_once()

    def test_view_tower(self):
        with patch.object(self.cli, 'view_generic', return_value=None) as mocked_view:
            self.cli.v_tower()
            mocked_view.assert_called_once_with(Tower)

# Operating System Tests
    @patch('builtins.input', side_effect=['1', 'Windows 10', 'Microsoft', '300'])
    def test_add_operatingsystem(self, mock_input):
        with patch.object(self.cli, 'add_generic', return_value=None) as mocked_add:
            self.cli.a_operatingsystem()
            mocked_add.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_delete_operatingsystem(self, mock_input):
        with patch.object(self.cli, 'delete_generic', return_value=None) as mocked_delete:
            self.cli.d_operatingsystem()
            mocked_delete.assert_called_once_with(OperatingSystem, 1)

    @patch('builtins.input', side_effect=['1', 'Updated OS', 'Linux', '350'])
    def test_edit_operatingsystem(self, mock_input):
        with patch.object(self.cli, 'edit_generic', return_value=None) as mocked_edit:
            self.cli.e_operatingsystem()
            mocked_edit.assert_called_once()

    def test_view_operatingsystems(self):
        with patch.object(self.cli, 'view_generic', return_value=None) as mocked_view:
            self.cli.v_operatingsystem()
            mocked_view.assert_called_once_with(OperatingSystem)

    # Monitor Tests
    @patch('builtins.input', side_effect=['1', 'Alienware 27', 'Alienware', '1200'])
    def test_add_monitor(self, mock_input):
        with patch.object(self.cli, 'add_generic', return_value=None) as mocked_add:
            self.cli.a_monitor()
            mocked_add.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_delete_monitor(self, mock_input):
        with patch.object(self.cli, 'delete_generic', return_value=None) as mocked_delete:
            self.cli.d_monitor()
            mocked_delete.assert_called_once_with(Monitor, 1)

    @patch('builtins.input', side_effect=['1', 'Updated Monitor', 'Samsung', '1800'])
    def test_edit_monitor(self, mock_input):
        with patch.object(self.cli, 'edit_generic', return_value=None) as mocked_edit:
            self.cli.e_monitor()
            mocked_edit.assert_called_once()

    def test_view_monitors(self):
        with patch.object(self.cli, 'view_generic', return_value=None) as mocked_view:
            self.cli.v_monitor()
            mocked_view.assert_called_once_with(Monitor)