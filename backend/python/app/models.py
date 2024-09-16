from django.db import models
import uuid


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(unique=True, null=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class Unit(AbstractModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Car(Unit):
    def save(self, *args, **kwargs):
        super(Car, self).save(*args, **kwargs)

        if not self.name:
            self.name = f"Car_{self.id}"
            super(Car, self).save(*args, **kwargs)
    


class Hotel(Unit):
    def save(self, *args, **kwargs):
        super(Hotel, self).save(*args, **kwargs)

        if not self.name:
            self.name = f"Hotel_{self.id}"
            super(Hotel, self).save(*args, **kwargs)
    

class Booking(AbstractModel):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)