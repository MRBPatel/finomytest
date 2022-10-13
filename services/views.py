from django.shortcuts import render

from .forms import LoanForm, HealthInsuranceForm, TaxReturnForm, VehicleInsuranceForm


# Create your views here.

def home(request):
    return render(request, 'index.html')


def home_loan(request):
    form = LoanForm()
    if request.method == 'POST':
        form = LoanForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'index.html')

        else:
            error = "Please enter the right information"
            return render(request, 'error.html', {error: 'error'})
    context = {
        'form': form,
    }
    return render(request, 'home_loan.html', context)


def health_insurance(request):
    health_form = HealthInsuranceForm()
    if request.method == 'POST':
        health_form = HealthInsuranceForm(request.POST)
        if health_form.is_valid():
            health_form.save()
            return render(request, 'index.html')

        else:
            error = "Please enter the right information"
            return render(request, 'error.html', {error: 'error'})

    context = {
        'form': health_form,
    }

    return render(request, 'insurance.html', context)


def vehicle_insurance(request):
    vehicle_form = VehicleInsuranceForm()
    if request.method == 'POST':
        vehicle_form = VehicleInsuranceForm(request.POST)
        if vehicle_form.is_valid():
            vehicle_form.save()
            return render(request, 'index.html')

        else:
            error = "Please enter the right information"
            return render(request, 'error.html', {error: 'error'})

    context = {
        'form': vehicle_form,
    }

    return render(request, 'insurance.html', context)


def tax_return(request):
    form = TaxReturnForm()
    if request.method == 'POST':
        form = TaxReturnForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'error.html')

        else:
            error = "Please enter the right information"
            return render(request, 'tax_return.html', {error: 'error'})
    context = {
        'form': form,
    }
    return render(request, 'tax_return.html', context)


def about(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact_us.html')
