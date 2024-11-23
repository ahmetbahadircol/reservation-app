from django.db import models
import uuid
from datetime import timedelta, datetime
from app.internal_api.api_functions import get_available_dates_for_unit
from reservation_app.utils import now


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(unique=True, null=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class Unit(AbstractModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def put_id_if_name_none(self, prefix="Unit"):
        if not self.name:
            self.name = f"{prefix}_{self.id}"
            self.update_fields.append("name")

    @property
    def bookings(self):
        return Booking.objects.filter(unit=self)

    @property
    def busy_dates(self) -> list[datetime.date]:
        return (
            self.bookings.filter(
                res_date__range=(
                    now().date(),
                    now() + timedelta(days=Booking.BOOKING_INTERVAL_DAY),
                )
            )
            .order_by("res_date")
            .values_list("res_date", flat=True)
        )

    def get_available_dates(
        self, request_dates: tuple[datetime.date]
    ):  # Take the request_dates as tuple for hashing
        # TODO: There is sometihng with this shit!!!
        request_dates = sorted(
            list(request_dates)
        )  # Because lists are not hashable, therefore we can't use caching
        response = get_available_dates_for_unit(
            request_dates=request_dates,
            busy_dates=self.busy_dates,
            days=Booking.BOOKING_INTERVAL_DAY,
        )
        if response.status_code == 200:
            return response.json()
        else:

            raise ValueError(
                f"go API has returned {response.status_code}: {response.json()}"
            )


class Car(Unit):
    def pre_save(self, *args, **kwargs):
        pass

    def post_save(self, *args, **kwargs):
        self.update_fields = []
        self.put_id_if_name_none("Car")
        super(Car, self).save(update_fields=self.update_fields)

    def save(self, *args, **kwargs):
        self.pre_save(*args, **kwargs)

        super(Car, self).save(*args, **kwargs)

        self.post_save(*args, **kwargs)


class Hotel(Unit):
    def pre_save(self, *args, **kwargs):
        pass

    def post_save(self, *args, **kwargs):
        self.update_fields = []
        self.put_id_if_name_none("Hotel")
        super(Hotel, self).save(update_fields=self.update_fields)

    def save(self, *args, **kwargs):
        self.pre_save(*args, **kwargs)

        super(Hotel, self).save(*args, **kwargs)

        self.post_save(*args, **kwargs)


class Booking(AbstractModel):
    BOOKING_INTERVAL_DAY = 30
    res_date = models.DateField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    @property
    def days(self) -> int:
        return self.BOOKING_INTERVAL_DAY
