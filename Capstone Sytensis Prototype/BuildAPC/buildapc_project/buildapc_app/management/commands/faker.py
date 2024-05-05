import random
from django.core.management.base import BaseCommand
from faker import Faker
from buildapc_app.models import CPU, Cooler, Motherboard, RAM, GPU, Storage, PowerSupply, Tower, OperatingSystem, Monitor

def random_sku():
    """Generate a random 23-digit integer as a string."""
    return str(random.randint(10**22, 10**23 - 1))

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **options):
        faker = Faker()

        # Populate CPUs
        for _ in range(10):
            CPU.objects.create(
                name=f'{faker.word()} {random.randint(100, 999)}',
                manufacturer=random.choice(['AMD', 'INTEL', 'TENCENT']),
                item_price=random.randint(250, 1000),
                vendor_sku=random_sku()
            )

        # Populate Coolers
        for _ in range(10):
            Cooler.objects.create(
                name=f'{faker.word()} Cooler',
                manufacturer=random.choice(['BeCool', 'Frozen', 'StayCool']),
                item_price=random.randint(100, 350),
                vendor_sku=random_sku()
            )

        # Populate Motherboards
        for _ in range(10):
            Motherboard.objects.create(
                name=f'{faker.word()} Motherboard',
                manufacturer=random.choice(['MSI', 'NZXT', 'iBuyPower']),
                item_price=random.randint(100, 400),
                vendor_sku=random_sku()
            )

        # Populate RAMs
        for _ in range(10):
            RAM.objects.create(
                name=f'{faker.word()} RAM',
                manufacturer=random.choice(['GForce', 'SpeedMe', 'TooFast']),
                item_price=random.randint(250, 550),
                vendor_sku=random_sku()
            )

        # Populate GPUs
        for _ in range(10):
            GPU.objects.create(
                name=f'{faker.word()} GPU',
                manufacturer=random.choice(['nVIDIA', 'AMD', 'FXT']),
                item_price=random.randint(700, 2300),
                vendor_sku=random_sku()
            )

        # Populate Storages
        for _ in range(10):
            Storage.objects.create(
                name=f'{faker.word()} Storage',
                manufacturer=random.choice(['Western Digital', 'Lucie', 'StoreIT']),
                item_price=random.randint(300, 900),
                vendor_sku=random_sku()
            )

        # Populate Power Supplies
        for _ in range(10):
            PowerSupply.objects.create(
                name=f'{faker.word()} PowerSupply',
                manufacturer=random.choice(['ChargeUp', 'NxtLVLEnergy', 'PositiveCHRG']),
                item_price=random.randint(200, 500),
                vendor_sku=random_sku()
            )

        # Populate Towers
        for _ in range(10):
            Tower.objects.create(
                name=f'{faker.word()} Tower',
                manufacturer=random.choice(['NZXT', 'Xteam', 'Valve']),
                item_price=random.randint(100, 250),
                vendor_sku=random_sku()
            )

        # Populate Operating Systems
        for _ in range(10):
            OperatingSystem.objects.create(
                name=f'{faker.word()} OS',
                manufacturer=random.choice(['Linux', 'Windows XP', 'Windows 11']),
                item_price=random.randint(100, 400),
                vendor_sku=random_sku()
            )

        # Populate Monitors
        for _ in range(10):
            Monitor.objects.create(
                name=f'{faker.word()} Monitor',
                manufacturer=random.choice(['Alienware', 'Samsung', 'LG']),
                item_price=random.randint(600, 1800),
                vendor_sku=random_sku()
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data'))

