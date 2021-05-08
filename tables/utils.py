from datetime import datetime

from tables.models import Reservation, WorkingHour


class IntervalValidation:
    def __init__(self, num_seats):
        self.working_hours = WorkingHour.objects.first()
        self.end_time = self.working_hours.end_day
        self.num_seats = num_seats
        self.time_now = datetime.now().time()
        self.start_time = self.get_start_time()

    def get_start_time(self):
        """

        update the start time if the start_day > now then the start time will be the start day
        if the start_day < now then the start time will be time_now
        """
        if self.working_hours.start_day > self.time_now:
            return self.working_hours.start_day
        else:
            return self.time_now

    def get_intervals(self):
        """

        retrieve today reservations  times for the table with the requested number of seats from the Reservation model
        the retrieved data must be made today and it is end time greater than the time now
        """
        exist_intervals = Reservation.objects.filter(reservation_date=datetime.now().date(),
                                                     end_time__gte=datetime.now().time(),

                                                     table__num_seats__range=[self.num_seats,
                                                                              self.num_seats + 1]).values(
            "start_time", "end_time")

        """
        check if there is no reservation for today 
        """
        if not exist_intervals:
            return [{"start_time": self.start_time, "end_time": "23:59"}]
        """
        check if there is no available time for the requested number of seats
        """
        if not exist_intervals.exclude(end_time__gte="23:59", start_time__lte=self.start_time):
            return []
        """
        if there is any reservations 
        """
        start_interval = {"start_time": self.start_time, "end_time": exist_intervals.first()["start_time"]}

        available_in = [start_interval]
        for index, interval in enumerate(exist_intervals):
            start = interval["end_time"]
            if index == len(exist_intervals) - 1:
                break
            end = exist_intervals[index + 1]["start_time"]
            interval = {"start_time": start, "end_time": end}
            available_in.append(interval)
        if self.end_time != exist_intervals.last()["end_time"]:
            available_in.append({"start_time": exist_intervals.last()["end_time"], "end_time": "23:59"})

        return available_in
