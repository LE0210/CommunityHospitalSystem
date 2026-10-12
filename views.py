from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from appointments.models import Appointment
from billing.models import Invoice
from lab.models import LabOrder


@login_required
def reports_index(request):
    from_date = request.GET.get('from', '2026-05-01')
    to_date = request.GET.get('to', '2026-05-12')
    dept = request.GET.get('dept', 'All')

    appts = Appointment.objects.filter(appointment_date__range=[from_date, to_date])
    invoices = Invoice.objects.filter(invoice_date__date__range=[from_date, to_date])
    labs = LabOrder.objects.filter(order_date__date__range=[from_date, to_date])

    return render(request, 'reports/index.html', {
        'total_patients': appts.values('patient').distinct().count(),
        'prescriptions_issued': appts.count(),  # placeholder — refine
        'labs_ordered': labs.count(),
        'no_show_rate': 0.0,  # compute from status == 'No-Show'
        'revenue': sum(i.total_amount for i in invoices),
    })