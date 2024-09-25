from django.utils import timezone
import pytz


def tz():
    return pytz.timezone("America/Toronto")


def now():
    current_local_time = timezone.now().astimezone(tz())
    return current_local_time
