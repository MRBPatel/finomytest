from django.contrib import admin
from .models import Loan, HealthInsurance, VehicleInsurance, TaxReturn

# Register your models here.
admin.site.register(Loan)
admin.site.register(HealthInsurance)
admin.site.register(TaxReturn)
admin.site.register(VehicleInsurance)
