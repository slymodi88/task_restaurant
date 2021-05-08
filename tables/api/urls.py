from django.urls import path
from tables.api.views import ReservationList,ReservationDetails,AvailableTimeApi


urlpatterns = [
    path('', ReservationList.as_view(), name='Reservations'),
    path('<int:pk>/', ReservationDetails.as_view(), name='Reservations'),
    path('available/', AvailableTimeApi.as_view(), name='Reservations'),

]