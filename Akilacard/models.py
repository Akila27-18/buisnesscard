# profile/models.py

import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField()
    image = models.ImageField(upload_to='profile_pics/')
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.qr_code:
            # Generate QR code
            qr = qrcode.make(self.linkedin)
            buffer = BytesIO()
            qr.save(buffer)
            filename = f"qr_{self.name.replace(' ', '_')}.png"
            self.qr_code.save(filename, File(buffer), save=False)
        super().save(*args, **kwargs)
