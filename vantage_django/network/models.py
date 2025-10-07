from django.db import models

class Record(models.Model):
    timestamp = models.DateTimeField()
    src_ip = models.CharField(max_length=64)
    dst_ip = models.CharField(max_length=64)
    proto = models.CharField(max_length=16, blank=True)
    src_port = models.IntegerField(null=True, blank=True)
    dst_port = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp} {self.src_ip}:{self.src_port} -> {self.dst_ip}:{self.dst_port} ({self.proto})"
