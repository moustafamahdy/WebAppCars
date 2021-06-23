from django.contrib import admin

from .models import *

# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display = ("StaffID", "first_name", "last_name", "PhoneNo")

class CarAdmin(admin.ModelAdmin):
    list_display = ("CarNo", "CarName", "CarModel", "staff")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("CustomerID", "PassportNo", "FirstName", "LastName", "address", "phone")

class RentalAdmin(admin.ModelAdmin):
    list_display = ("RentalNO", "CarNo", "StaffID", "CustomerId", "Timeout", "TimeReturn")
    

admin.site.register(Staff, StaffAdmin)
admin.site.register(Car,CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rental, RentalAdmin)