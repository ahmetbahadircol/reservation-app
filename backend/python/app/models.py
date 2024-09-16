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
    
    def put_id_if_name_none(self, prefix="Unit"):
        if not self.name:
            self.name = f"{prefix}_{self.id}"


class Car(Unit):
    def pre_save(self, *args, **kwargs):
        pass

    def post_save(self, *args, **kwargs):
        self.put_id_if_name_none("Car")
        super(Car, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.pre_save(*args, **kwargs)

        super(Car, self).save(*args, **kwargs)

        self.post_save(*args, **kwargs)
    


class Hotel(Unit):
    def pre_save(self, *args, **kwargs):
        pass

    def post_save(self, *args, **kwargs):
        self.put_id_if_name_none("Hotel")
        super(Car, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.pre_save(*args, **kwargs)

        super(Car, self).save(*args, **kwargs)

        self.post_save(*args, **kwargs)
    

class Booking(AbstractModel):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)