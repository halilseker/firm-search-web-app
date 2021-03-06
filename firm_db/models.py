# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse

class Company(models.Model):
    firm_title = models.TextField(blank=True, null=True)
    firm_representative = models.TextField(blank=True, null=True)
    firm_phone_number = models.TextField(blank=True, null=True)
    firm_email = models.TextField(blank=True, null=True)
    firm_address = models.TextField(blank=True, null=True)
    firm_services = models.TextField(blank=True, null=True)
    firm_mobile_number = models.TextField(blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'company'

    def __str__(self):
        return self.firm_title

    def get_absolute_url(self):
        return reverse('firm_db_detail', args=[str(self.id)])
