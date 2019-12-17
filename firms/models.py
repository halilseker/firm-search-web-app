from django.db import models


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
