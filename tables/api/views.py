from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from tables.models import Reservation
from tables.api.serializers import ReservationSerializer, AvailableTimes
from rest_framework import filters
from mixins.paginator import CustomPagination
from datetime import date, datetime
from rest_framework.permissions import IsAuthenticated
from tables.utils import IntervalValidation


class AvailableTimeApi(generics.ListAPIView):
    """
    AvailableTimeApi used to to retrieve the available time of a table during the working day

    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def list(self, request, *args, **kwargs):
        """

        num_seats query param used to check that the requested number of seats in a reservation don't exceed the maximum
         number of seats in the restaurant
         intervals calls get_available_interval() functions that calculates available time slots
        """
        num_seats = int(self.request.query_params.get('num_seats'))
        if num_seats <= 6:
            intervals = IntervalValidation(num_seats).get_intervals()
            serializer = AvailableTimes(intervals, many=True)
            return Response({"result": serializer.data, "message": "Done", "status": True}, status=200)
        return Response({"message": "NO Tables Available", "status": False}, status=400)


class ReservationList(generics.ListCreateAPIView):
    """
    ReservationList api to list all the reservations in the current day and book an available reservation time
    filter_backends and  ordering_fields to allow the user to order the results by start time or end time
    pagination class used to list the results in a paginated way
    permission_classes to make sure only logged users can use the api
    """
    queryset = Reservation.objects.filter(reservation_date=date.today())
    serializer_class = ReservationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['start_time', 'end_time']
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(self.filter_queryset(self.queryset))
        serializer = ReservationSerializer(queryset, many=True)
        return self.paginator.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data, "message": "Done", "status": True}, status=201)
        return Response({"message": serializer.errors, "status": False}, status=400)


class ReservationDetails(generics.DestroyAPIView):
    """
    ReservationDetails used to delete an upcoming reservation using reservation id
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        reservation = get_object_or_404(Reservation, id=kwargs["pk"])
        if reservation.reservation_date < date.today():
            return Response({"message": "Not Allowed To Delete This Reservation", "status": False}, status=400)
        reservation.delete()
        return Response({"message": "Done", "status": True}, status=200)
