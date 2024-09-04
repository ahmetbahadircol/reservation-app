from django.db import models
import uuid


class AbstractModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(unique=True, null=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class Unit(AbstractModel):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class Car(Unit):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"Car_{id}"
        return super(Car, self).save(*args, **kwargs)
    


class Hotel(Unit):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"Hotel_{id}"
        return super(Car, self).save(*args, **kwargs)