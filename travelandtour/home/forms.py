from django import forms
from .models import Staff


class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ('name', 'address', 'phone_number',
                'email', 'join_date', 'salary', 'staff_img', 'role_id', 'company_id', 'package_guide')