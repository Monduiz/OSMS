from django import forms
from .models import Trip, Hoir, Oscr, Closeout, Office
from .utils import create_trip_link, create_work_addr

TRIPS_HOIR_LINK = create_trip_link()
TRIP_CHOICES = [("", "Choose activity")] + [(t['id'], t['trip_description']) for t in TRIPS_HOIR_LINK]
WORKPLACES = create_work_addr()
# Create an empty option and add to the list of dictionaries
# The list is transformed into a key value pair tuples for the select options
WORKPLACE_CHOICES = [("", "Choose workplace")] + [(li['address'], li['address']) for li in WORKPLACES]
REGIONS = list(set([r['region'] for r in WORKPLACES]))
REGION_CHOICES = [("", "Choose region")] + [(r, r) for r in REGIONS]

# hoir_fields = [f.name for f in Hoir._meta.fields]
# hoir_fields = [e for e in hoir_fields if e not in ('id', 'date_created')]

class HoirForm(forms.ModelForm):
    work_address = forms.ChoiceField(choices = WORKPLACE_CHOICES)
    region = forms.ChoiceField(choices = REGION_CHOICES)
    mail_address = forms.ChoiceField(choices = WORKPLACE_CHOICES)
    trip_id = forms.ChoiceField(choices = TRIP_CHOICES, required=False)

    class Meta:
        model = Hoir
        fields = '__all__'
        exclude = ['id', 'officer', 'date_created']

class OscrForm(forms.ModelForm):
    region = forms.ChoiceField(choices = REGION_CHOICES)
    trip_id = forms.ChoiceField(choices = TRIP_CHOICES, required=False)

    class Meta:
        model = Oscr
        fields = '__all__'
        exclude = ['id', 'officer', 'date_created']

class CloseoutForm(forms.ModelForm):
    trip_id = forms.ChoiceField(choices = TRIP_CHOICES, required=False)

    class Meta:
        model = Closeout
        fields = '__all__'
        exclude = ['id', 'officer', 'date_created']
