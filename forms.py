from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender',
                  'id_number', 'phone_number', 'email_address',
                  'physical_address', 'blood_type', 'medical_aid_provider',
                  'medical_aid_number', 'emergency_contact_name',
                  'emergency_contact_phone']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'physical_address': forms.Textarea(attrs={'rows': 2}),
        }

    def clean_id_number(self):
        idn = self.cleaned_data['id_number']
        if not idn.isdigit() or len(idn) != 13:
            raise forms.ValidationError("ID number must be exactly 13 digits.")
        return idn