from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="mainpage"),
    path("cars/", views.CarsList.as_view(), name="cars"),
    path("createCar/", views.CreateCar.as_view(), name="createcar"),
    path("cars/<int:pk>/", views.CarDetails.as_view(), name="cardetails"),
    path("cars/<int:pk>/delete", views.DeleteCar.as_view(), name="cardelete"),

    path("staffs/", views.StaffsList.as_view(), name="staffs"),
    path("createstaff/", views.CreateStaff.as_view(), name="createstaff"),
    path("staffs/<int:pk>/", views.StaffDetails.as_view(), name="staffdetails"),
    path("staffs/<int:pk>/delete", views.DeleteStaff.as_view(), name="staffdelete"),

    path("customers/", views.CutomersList.as_view(), name="customers"),
    path("createcustomer/", views.CreateCustomer.as_view(), name="createcustomer"),
    path("customers/<int:pk>/", views.CustomerDetails.as_view(), name="customerdetails"),
    path("customers/<int:pk>/delete", views.DeleteCustomer.as_view(), name="customerdelete"),

    path("rentals/", views.RentalsList.as_view(), name="rentals"),
    path("createrental/", views.CreateRental.as_view(), name="createrental"),
    path("rentals/<int:pk>/", views.RentalDetails.as_view(), name="rentaldetails"),
    path("rentals/<int:pk>/delete", views.DeleteRental.as_view(), name="rentaldelete"),

]