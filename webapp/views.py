from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.reverse import reverse
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import HTMLFormRenderer, TemplateHTMLRenderer
from django.http import Http404
from rest_framework import mixins, generics

# Create your views here.
def index(request):
    return render(request, "webapp/mainpage.html")

class CarsList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "webapp/cars.html"

    def get(self,request):

        queryset = Car.objects.all()

        return Response({
            "cars": queryset
        })

class CreateCar(mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Car.objects.all()
    serializer_class =  CarSerializer

    def post(self, request):
        self.create(request)
        return HttpResponseRedirect(reverse('cars'))

class CarDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "webapp/car.html"

    def get(self, request, pk):
        
        car = get_object_or_404(Car, pk = pk)
        serializer = CarSerializer(car)

        return Response({
            "serializer": serializer,
            "car": car
        })

    def post(self, request, pk):
        
        car = get_object_or_404(Car, pk = pk)
        serializer = CarSerializer(car, data = request.data)

        if not serializer.is_valid():
            return Response({
                "serializer": serializer,
                "car": car
            })

class DeleteCar(APIView):

    def  get_Car(self, pk):
        try:
            return Car.objects.get(pk= pk)
        except Car.DoesNotExist:
            raise Http404

    def delete(self, request, pk, *args):
        car = self.get_Car(pk)
        car.delete()
        return HttpResponseRedirect(reverse('cars'))

class StaffsList(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "webapp/staffs.html"

    def get(self, request):

        queryset = Staff.objects.all()

        return Response({
            "staffs": queryset
        })


class CreateStaff(mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Staff.objects.all()
    serializer_class =  StaffSerilalizer

    def post(self, request):
        self.create(request)
        return HttpResponseRedirect(reverse('staffs'))

class StaffDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "webapp/staff.html"

    def get(self, request, pk):
        
        staff = get_object_or_404(Staff, pk = pk)
        serializer = StaffSerilalizer(staff)

        return Response({
            "serializer": serializer,
            "staff": staff
        })

    def post(self, request, pk):
        
        staff = get_object_or_404(Staff, pk = pk)
        serializer = StaffSerilalizer(staff, data = request.data)

        if not serializer.is_valid():
            return Response({
                "serializer": serializer,
                "staff": staff
            })

class DeleteStaff(APIView):

    def  get_Staff(self, pk):
        try:
            return Staff.objects.get(pk= pk)
        except Staff.DoesNotExist:
            raise Http404

    def delete(self, request, pk, *args):
        staff = self.get_Staff(pk)
        staff.delete()
        return HttpResponseRedirect(reverse('staffs'))

class CutomersList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "webapp/customers.html"

    def get (self, request):

        queryset = Customer.objects.all()

        return Response({
            "customers": queryset
        })

class CreateCustomer(mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Customer.objects.all()
    serializer_class =  CustomerSerializer

    def post(self, request):
        self.create(request)
        return HttpResponseRedirect(reverse('customers'))

class CustomerDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "webapp/customer.html"

    def get(self, request, pk):
        
        customer = get_object_or_404(Customer, pk = pk)
        serializer = CustomerSerializer(customer)

        return Response({
            "serializer": serializer,
            "customer": customer
        })

    def post(self, request, pk):
        
        customer = get_object_or_404(Customer, pk = pk)
        serializer = CustomerSerializer(customer, data = request.data)

        if not serializer.is_valid():
            return Response({
                "serializer": serializer,
                "customer": customer
            })

class DeleteCustomer(APIView):

    def  get_Customer(self, pk):
        try:
            return Customer.objects.get(pk= pk)
        except Customer.DoesNotExist:
            raise Http404

    def delete(self, request, pk, *args):
        customer = self.get_Customer(pk)
        customer.delete()
        return HttpResponseRedirect(reverse('customers'))

class RentalsList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "webapp/rentals.html"

    def get (self, request):

        queryset = Rental.objects.all()

        return Response({
            "rentals": queryset
        })

class CreateRental(mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Rental.objects.all()
    serializer_class =  RentalSerializer

    def post(self, request):
        self.create(request)
        return HttpResponseRedirect(reverse('rentals'))

class RentalDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "webapp/rental.html"

    def get(self, request, pk):
        
        rental = get_object_or_404(Rental, pk = pk)
        serializer = RentalSerializer(rental)

        return Response({
            "serializer": serializer,
            "rental": rental
        })

    def post(self, request, pk):
        
        rental = get_object_or_404(Rental, pk = pk)
        serializer = RentalSerializer(rental, data = request.data)

        if not serializer.is_valid():
            return Response({
                "serializer": serializer,
                "rental": rental
            })

class DeleteRental(APIView):

    def  get_Rental(self, pk):
        try:
            return Rental.objects.get(pk= pk)
        except Rental.DoesNotExist:
            raise Http404

    def delete(self, request, pk, *args):
        rental = self.get_Rental(pk)
        rental.delete()
        return HttpResponseRedirect(reverse('rentals'))