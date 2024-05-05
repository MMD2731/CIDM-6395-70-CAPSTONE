from rest_framework import serializers
from .models import (
    CPU, Cooler, Motherboard, RAM, GPU, Storage, PowerSupply, Tower, 
    OperatingSystem, Monitor, Product, ProductType, SystemIntegrator, 
    BuildAPC_Config, Customer, Review, CustomerWishList, HumanResource
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CPUSerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)  # Nested Product details

    class Meta:
        model = CPU
        fields = '__all__'

class CoolerSerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = Cooler
        fields = '__all__'

class MotherboardSerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = Motherboard
        fields = '__all__'

class RAMSerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = RAM
        fields = '__all__'

class GPUSerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = GPU
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = Storage
        fields = '__all__'

class PowerSupplySerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = PowerSupply
        fields = '__all__'

class TowerSerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = Tower
        fields = '__all__'

class OperatingSystemSerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = OperatingSystem
        fields = '__all__'

class MonitorSerializer(serializers.ModelSerializer):
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = Monitor
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # Nested relationship to show products

    class Meta:
        model = ProductType
        fields = '__all__'

class SystemIntegratorSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer(read_only=True)
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = SystemIntegrator
        fields = '__all__'

class BuildAPC_ConfigSerializer(serializers.ModelSerializer):
    system_integrator = SystemIntegratorSerializer(read_only=True)
    product_type = ProductTypeSerializer(read_only=True)
    vendor_sku = ProductSerializer(read_only=True)

    class Meta:
        model = BuildAPC_Config
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class CustomerWishListSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    product_type = ProductTypeSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CustomerWishList
        fields = '__all__'

class HumanResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanResource
        fields = '__all__'