from django.db import models
from djnago.urls import reverse

class Firm(models.Model):
    firm_title = models.TextField()
    firm_representative = models.TextField()
    firm_phone_number = models.TextField()
    firm_email = models.TextField()
    firm_address = models.TextField()
    firm_services = models.TextField()
    firm_mobile_number = models.TextField()

    def __str__(self):
        return self.firm_title

    def get_absolute_url(self):
        return reverse('firm_detail', args=[str(self.id)])
