from django.db import models
import uuid
from datetime import timedelta
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
    #TODO: Spesifik bir booking objesi için start ve end date aralığındaki günlerin listesini çıkar. Ardından 30 günlük period içinde o günlerinde dışındaki günleri liste halinde dön.
    import requests


    BOOKING_INTERVAL_DAY = 30
    start_date = models.DateField()
    end_date = models.DateField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    @property
    def days(self):
        return self.BOOKING_INTERVAL_DAY
    
    @property
    def calculate_interval_date_list(self):
        return [(now() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(self.days)]
    
    @property
    def get_free_dates(self):
        qs = Booking.objects.filter(start_date__gte=now(), end_date__lte=now() + timedelta(days=self.BOOKING_INTERVAL_DAY), unit=self.unit).values_list()
        return list(qs)
    
    @property
    def get_available_days(self, request_dates: list[str]):
        payload = {
            "days": self.days,
            "request_days": request_dates,

        }