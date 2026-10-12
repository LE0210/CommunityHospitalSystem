from django.core.management.base import BaseCommand
from accounts.models import Staff
from pharmacy.models import Medication, Inventory


class Command(BaseCommand):
    help = 'Seed demo data'

    def handle(self, *args, **opts):
        Staff.objects.get_or_create(staff_id='DR001', defaults={
            'username': 'dr001', 'first_name': 'Aisha', 'last_name': 'Naidoo',
            'role': 'Doctor', 'specialty': 'General Practice', 'email': 'aisha@cgh.co.za',
        })
        Staff.objects.get_or_create(staff_id='PH001', defaults={
            'username': 'ph001', 'first_name': 'Lerato', 'last_name': 'Fortuin',
            'role': 'Pharmacist', 'email': 'lerato@cgh.co.za',
        })
        meds = [
            ('Metformin 500mg', 'MED001', 'Antidiabetic', 'tablet', 50),
            ('Amlodipine 5mg', 'MED002', 'Antihypertensive', 'tablet', 50),
            ('Paracetamol 500mg', 'MED003', 'Analgesic', 'tablet', 100),
        ]
        for name, code, cat, unit, reorder in meds:
            m, _ = Medication.objects.get_or_create(drug_code=code, defaults={
                'drug_name': name, 'category': cat, 'unit_of_measure': unit,
                'reorder_level': reorder,
            })
            Inventory.objects.get_or_create(medication=m, defaults={'quantity': 200})
        self.stdout.write(self.style.SUCCESS('Seed data created'))