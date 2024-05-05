from django.core.management.base import BaseCommand
import cmd
from getpass import getpass
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from buildapc_app.models import CPU, Cooler, Motherboard, RAM, GPU, Storage, PowerSupply, Tower, OperatingSystem, Monitor, Product

class BuildAPCAdminCLI(cmd.Cmd):
    intro = 'Welcome to the BuildAPC Admin Console. Type help or ? to list commands.'
    prompt = 'Enter Username'

    def do_login(self, line):
        username = input("Username: ")
        password = getpass("Password: ")
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser:
            print("Login successful.")
            self.prompt = f'(buildapc:{username}) '
        else:
            print("Login failed.")
            return True  # Exit the program if login fails

    def do_quit(self, arg):
        """Exits the application."""
        print("Thank you for using BuildAPC Admin Console.")
        return True  # Return True to stop the cmd loop and exit

    def main_menu(self):
        options = {
            "1": "CPU",
            "2": "Cooler",
            "3": "Motherboard",
            "4": "RAM",
            "5": "GPU",
            "6": "Storage",
            "7": "PowerSupply",
            "8": "Tower",
            "9": "OperatingSystem",
            "0": "Monitor",
            "Q": "Quit"
        }
        while True:
            print("\nPC Component Admin View")
            for key, value in options.items():
                print(f"({key}) {value}")
            choice = input("Select a component to manage or Q to Quit: ").upper()
            if choice == 'Q':
                print("Exiting the program.")
                break
            elif choice in options:
                self.component_menu(options[choice])
            else:
                print("Invalid choice, try again.")

    def component_menu(self, component):
        actions = {
            "A": "Add",
            "D": "Delete",
            "E": "Edit",
            "V": "View",
            "Q": "Quit to Main Menu"
        }
        while True:
            print(f"\n{component} Management")
            for key, value in actions.items():
                print(f"({key}) {value}")
            action = input("Choose an action or Q to Quit to Main Menu: ").upper()
            if action == 'Q':
                break
            elif action in actions:
                func_name = f"{action.lower()}_{component.lower()}"
                if hasattr(self, func_name):
                    getattr(self, func_name)()
                else:
                    print("Action not implemented.")
            else:
                print("Invalid action, try again.")

    def add_generic(self, model, **kwargs):
        try:
            vendor_sku_id = int(input("Enter Vendor SKU ID: "))
            name = input("Enter Name: ")
            manufacturer = input("Enter Manufacturer: ")
            item_price = float(input("Enter Item Price: "))
            product = Product.objects.get(vendor_sku=vendor_sku_id)
            obj = model(vendor_sku=product, name=name, manufacturer=manufacturer, item_price=item_price)
            obj.save()
            print(f"{model.__name__} added successfully.")
        except Product.DoesNotExist:
            print("Error: Product with provided SKU does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_generic(self, model, component_id):
        try:
            obj = model.objects.get(pk=component_id)
            obj.delete()
            print(f"{model.__name__} deleted successfully.")
        except model.DoesNotExist:
            print(f"{model.__name__} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def edit_generic(self, model, component_id, **kwargs):
        try:
            obj = model.objects.get(pk=component_id)
            for key, value in kwargs.items():
                setattr(obj, key, value or getattr(obj, key))
            obj.save()
            print(f"{model.__name__} updated successfully.")
        except model.DoesNotExist:
            print(f"{model.__name__} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_generic(self, model):
        objects = model.objects.all()
        for obj in objects:
            print(f"ID: {obj.pk}, Name: {obj.name}, Manufacturer: {obj.manufacturer}, Price: {obj.item_price}")

    # CRUD methods for each component, below are examples for CPU
    def a_cpu(self):
        self.add_generic(CPU)

    def d_cpu(self):
        cpu_id = int(input("Enter CPU ID to delete: "))
        self.delete_generic(CPU, cpu_id)

    def e_cpu(self):
        cpu_id = int(input("Enter CPU ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(CPU, cpu_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_cpu(self):
        self.view_generic(CPU)

    # Cooler
    def a_cooler(self):
        self.add_generic(Cooler)

    def d_cooler(self):
        cooler_id = int(input("Enter Cooler ID to delete: "))
        self.delete_generic(Cooler, cooler_id)

    def e_cooler(self):
        cooler_id = int(input("Enter Cooler ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(Cooler, cooler_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_cooler(self):
        self.view_generic(Cooler)

    # Motherboard
    def a_motherboard(self):
        self.add_generic(Motherboard)

    def d_motherboard(self):
        mb_id = int(input("Enter Motherboard ID to delete: "))
        self.delete_generic(Motherboard, mb_id)

    def e_motherboard(self):
        mb_id = int(input("Enter Motherboard ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(Motherboard, mb_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_motherboard(self):
        self.view_generic(Motherboard)

    # RAM
    def a_ram(self):
        self.add_generic(RAM)

    def d_ram(self):
        ram_id = int(input("Enter RAM ID to delete: "))
        self.delete_generic(RAM, ram_id)

    def e_ram(self):
        ram_id = int(input("Enter RAM ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(RAM, ram_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_ram(self):
        self.view_generic(RAM)

    # GPU
    def a_gpu(self):
        self.add_generic(GPU)

    def d_gpu(self):
        gpu_id = int(input("Enter GPU ID to delete: "))
        self.delete_generic(GPU, gpu_id)

    def e_gpu(self):
        gpu_id = int(input("Enter GPU ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(GPU, gpu_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_gpu(self):
        self.view_generic(GPU)

    # Storage
    def a_storage(self):
        self.add_generic(Storage)

    def d_storage(self):
        storage_id = int(input("Enter Storage ID to delete: "))
        self.delete_generic(Storage, storage_id)

    def e_storage(self):
        storage_id = int(input("Enter Storage ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(Storage, storage_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_storage(self):
        self.view_generic(Storage)

    # PowerSupply
    def a_powersupply(self):
        self.add_generic(PowerSupply)

    def d_powersupply(self):
        ps_id = int(input("Enter PowerSupply ID to delete: "))
        self.delete_generic(PowerSupply, ps_id)

    def e_powersupply(self):
        ps_id = int(input("Enter PowerSupply ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(PowerSupply, ps_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_powersupply(self):
        self.view_generic(PowerSupply)

    # Tower
    def a_tower(self):
        self.add_generic(Tower)

    def d_tower(self):
        t_id = int(input("Enter Tower ID to delete: "))
        self.delete_generic(Tower, t_id)

    def e_tower(self):
        t_id = int(input("Enter Tower ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(Tower, t_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_tower(self):
        self.view_generic(Tower)

    # OperatingSystem
    def a_operatingsystem(self):
        self.add_generic(OperatingSystem)

    def d_operatingsystem(self):
        os_id = int(input("Enter Operating System ID to delete: "))
        self.delete_generic(OperatingSystem, os_id)

    def e_operatingsystem(self):
        os_id = int(input("Enter Operating System ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(OperatingSystem, os_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_operatingsystem(self):
        self.view_generic(OperatingSystem)

    # Monitor
    def a_monitor(self):
        self.add_generic(Monitor)

    def d_monitor(self):
        mon_id = int(input("Enter Monitor ID to delete: "))
        self.delete_generic(Monitor, mon_id)

    def e_monitor(self):
        mon_id = int(input("Enter Monitor ID to edit: "))
        name = input("Enter new name: ")
        manufacturer = input("Enter new manufacturer: ")
        item_price = float(input("Enter new item price: "))
        self.edit_generic(Monitor, mon_id, name=name, manufacturer=manufacturer, item_price=item_price)

    def v_monitor(self):
        self.view_generic(Monitor)


class Command(BaseCommand):
    help = 'Starts the BuildAPC command line interface.'

    def handle(self, *args, **options):
        cli = BuildAPCAdminCLI()
        cli.main_menu()

if __name__ == '__main__':
    BuildAPCAdminCLI().cmdloop()


