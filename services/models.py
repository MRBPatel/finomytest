from django.db import models
from django.core.validators import RegexValidator
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Loan(models.Model):
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=15)

    NONE = "None"
    HOME = "Home Loan"
    MACHINE = "Machine Loan"
    STUDENT = "Student Loan"
    OTHER = "Other Loan"
    LOAN_CHOICES = (
        (HOME, "Home Loan"),
        (MACHINE, "Machine Loan"),
        (STUDENT, "Student Loan"),
        (OTHER, "Other Loan")
    )

    loan_type = models.CharField(max_length=20, choices=LOAN_CHOICES)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    customer_mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators
    # should be a list
    customer_email = models.EmailField(max_length=65)

    def __str__(self):
        return self.customer_first_name


class HealthInsurance(models.Model):
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=15)
    family_members = models.IntegerField()
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6, default="394180")

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    customer_mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators
    # should be a list
    customer_email = models.EmailField(max_length=65)

    def __str__(self):
        return self.customer_first_name


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class VehicleInsurance(models.Model):
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=15)
    vehicle_brand = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)

    PETROL = "PETROL"
    DIESEL = "DIESEL"
    CNG = "CNG"
    ELECTRIC = "ELECTRIC"
    TYPE_CHOICES = (
        (PETROL, "PETROL"),
        (DIESEL, "DIESEL"),
        (CNG, "CNG"),
        (ELECTRIC, "ELECTRIC")
    )

    fuel_type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    registration_year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1996), max_value_current_year])
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6, default="394180")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    customer_mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators
    # should be a list
    customer_email = models.EmailField(max_length=65)

    def __str__(self):
        return self.customer_first_name


class TaxReturn(models.Model):
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=15)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    customer_mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators
    # should be a list
    customer_email = models.EmailField(max_length=65)

    def __str__(self):
        return self.customer_first_name
