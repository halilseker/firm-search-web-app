from django.contrib import admin
from .models import Firm


class FirmAdmin(admin.ModelAdmin):
    list_display = ("firm_title", "firm_representative",
                    "firm_phone_number","firm_mobile_number", "firm_address",
                    "firm_email","firm_services")

admin.site.register(Firm, FirmAdmin)
