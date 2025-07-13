from django.db import models
from django.utils import timezone
import string,random

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortURL(models.Model):
    url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_code)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.url}"

