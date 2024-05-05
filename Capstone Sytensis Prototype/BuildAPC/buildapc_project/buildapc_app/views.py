from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

# Import models and serializers 
from .models import (
    CPU, Cooler, Motherboard, RAM, GPU, Storage, PowerSupply, Tower,
    OperatingSystem, Monitor, Product, ProductType, SystemIntegrator,
    BuildAPC_Config, Customer, Review, CustomerWishList, HumanResource
)
from .serializers import (
    CPUSerializer, CoolerSerializer, MotherboardSerializer, RAMSerializer,
    GPUSerializer, StorageSerializer, PowerSupplySerializer, TowerSerializer,
    OperatingSystemSerializer, MonitorSerializer, ProductSerializer,
    ProductTypeSerializer, SystemIntegratorSerializer, BuildAPC_ConfigSerializer,
    CustomerSerializer, ReviewSerializer, CustomerWishListSerializer, HumanResourceSerializer
)

class GenericAPIView(APIView):
    model = None
    serializer = None

    def get_object(self, model, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            instance = self.get_object(self.model, pk)
            serializer = self.serializer(instance)
        else:
            instances = self.model.objects.all()
            serializer = self.serializer(instances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        instance = self.get_object(self.model, pk)
        serializer = self.serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(self.model, pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Define views for each model
class CPUView(GenericAPIView):
    model = CPU
    serializer = CPUSerializer

class CoolerView(GenericAPIView):
    model = Cooler
    serializer = CoolerSerializer

class MotherboardView(GenericAPIView):
    model = Motherboard
    serializer = MotherboardSerializer

class RAMView(GenericAPIView):
    model = RAM
    serializer = RAMSerializer

class GPUView(GenericAPIView):
    model = GPU
    serializer = GPUSerializer

class StorageView(GenericAPIView):
    model = Storage
    serializer = StorageSerializer

class PowerSupplyView(GenericAPIView):
    model = PowerSupply
    serializer = PowerSupplySerializer

class TowerView(GenericAPIView):
    model = Tower
    serializer = TowerSerializer

class OperatingSystemView(GenericAPIView):
    model = OperatingSystem
    serializer = OperatingSystemSerializer

class MonitorView(GenericAPIView):
    model = Monitor
    serializer = MonitorSerializer

class ProductView(GenericAPIView):
    model = Product
    serializer = ProductSerializer

class ProductTypeView(GenericAPIView):
    model = ProductType
    serializer = ProductTypeSerializer

class SystemIntegratorView(GenericAPIView):
    model = SystemIntegrator
    serializer = SystemIntegratorSerializer

class BuildAPC_ConfigView(GenericAPIView):
    model = BuildAPC_Config
    serializer = BuildAPC_ConfigSerializer

class CustomerView(GenericAPIView):
    model = Customer
    serializer = CustomerSerializer

class ReviewView(GenericAPIView):
    model = Review
    serializer = ReviewSerializer

class CustomerWishListView(GenericAPIView):
    model = CustomerWishList
    serializer = CustomerWishListSerializer

class HumanResourceView(GenericAPIView):
    model = HumanResource
    serializer = HumanResourceSerializer

# Admin + User Logins 
def admin_check(user):
    return user.groups.filter(name='Administrator').exists()

def user_check(user):
    return user.groups.filter(name='User').exists()

@login_required
@user_passes_test(admin_check)
def admin_home(request):
    return render(request, 'admin_home.html')

@login_required
@user_passes_test(user_check)
def user_home(request):
    return render(request, 'user_home.html')