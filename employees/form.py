import datetime

from django.forms import SelectDateWidget

from .models import EmployeeModel
from django import forms


class EmployeesFormForIdForm(forms.Form):
    id = forms.IntegerField(min_value=1,
                            label='id')

class EmployeesFormForNameForm(forms.Form):
    name = forms.CharField(max_length=100,
                              label='Имя')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'

        widgets = {
            'date_of_hiring': SelectDateWidget(years=range(1990, 2030), empty_label=datetime.datetime.now())
        }

