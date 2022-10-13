from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Loan, HealthInsurance, VehicleInsurance, TaxReturn


class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = ['customer_first_name', 'customer_last_name',
                  'loan_type', 'customer_mobile_number',
                  'customer_email']
        labels = {
            'customer_first_name': _('First Name'),
            'customer_last_name': _('Last Name'),
            'customer_mobile_number': _('Mobile Number'),
            'customer_email': _('Email Address'),
        }


class HealthInsuranceForm(ModelForm):
    class Meta:
        model = HealthInsurance
        fields = ['customer_first_name', 'customer_last_name',
                  'family_members', 'city', 'zip_code',
                  'customer_mobile_number', 'customer_email']
        labels = {
            'customer_first_name': _('First Name'),
            'customer_last_name': _('Last Name'),
            'customer_mobile_number': _('Mobile Number'),
            'customer_email': _('Email Address'),
        }


class VehicleInsuranceForm(ModelForm):
    class Meta:
        model = VehicleInsurance
        fields = ['customer_first_name', 'customer_last_name',
                  'vehicle_brand', 'vehicle_model', 'fuel_type',
                  'registration_year', 'city', 'zip_code', 'customer_mobile_number',
                  'customer_email']
        labels = {
            'customer_first_name': _('First Name'),
            'customer_last_name': _('Last Name'),
            'customer_mobile_number': _('Mobile Number'),
            'customer_email': _('Email Address'),
        }


class TaxReturnForm(ModelForm):
    class Meta:
        model = TaxReturn
        fields = '__all__'
        labels = {
            'customer_first_name': _('First Name'),
            'customer_last_name': _('Last Name'),
            'customer_mobile_number': _('Mobile Number'),
            'customer_email': _('Email Address')
        }
        error_messages = {
            'customer_mobile_number': {
                'max_length': _("Please enter a valid mobile number"),
            },
        }
