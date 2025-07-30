# profile/signals.py

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Profile

import qrcode
from io import BytesIO
from django.core.files import File

@receiver(pre_save, sender=Profile)
def generate_qr_code(sender, instance, **kwargs):
    if not instance.qr_code:
        qr = qrcode.make(instance.linkedin)
        buffer = BytesIO()
        qr.save(buffer)
        filename = f"qr_{instance.name.replace(' ', '_')}.png"
        instance.qr_code.save(filename, File(buffer), save=False)
