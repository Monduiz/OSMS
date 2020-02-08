from django.contrib.gis.db import models
from django.utils import timezone
from users.models import User
from django.conf import settings
from django.urls import reverse


REGS = ('', '2BER', 'AMMRR', 'BIGR', 'CAMRR')
PARTNERS = ('', 'CBSA', 'DFO', 'International', 'OGD', 'Parks Canada', 'Provincial',
            'RCMP', 'Territorial', 'USFWS')
LEGS = ('', 'FA', 'CEPA', 'FA and CEPA')
PURPOSES = ('', 'Planned inspection', 'Unplanned inspection', 'Surveillance',
    'Production order', 'Serving court documents', 'Enforcement action',
    'Undercover operation', 'General warrant','Warrant', 'Interview','Other')
INTEL_REPORT = ('', 'Yes', 'No')
RISK_LOCATIONS = ('', 'Urban', 'Rural', 'Remote', 'Isolated', 'Marine')
RISK_LOC_FAM = ('', 'Known', 'Unfamiliar', 'Unknown', 'Public area')
RISK_TIME_CHOICES = ('', 'Daytime (30 min after sunrise)', 'Dusk or Dawn', 'Night (30 min after sunset)')
RISK_WEATHER_CHOICES = ('', 'Clear', 'Mildly inclement', 'Severely inclement', 'Unknown')
RISK_TERRAIN_CHOICES = ('', 'Dry land', 'Mud / Wet lands', 'Rivers / Lakes', 'Ocean', 'Mountains')
RISK_COMM_CHOICES = ('', 'Cell / PTT/ Radio', 'Satelite', 'No comms')
RISK_EMERGENCY_CHOICES = ('', 'Fast (<15 mins)', 'Medium (15-30 mins)', 'Slow (>30 mins)')
RISK_DISTANCE_CHOICES = ('', 'Close', 'Medium', 'Far')
RISK_TRANSPORT_CHOICES = ('', 'Low', 'Medium', 'High')
RISK_CRIMINAL_CHOICES = ('', 'No', 'Corporate', 'Violent')
RISK_COMPLIANCE_CHOICES = ('', 'No', 'Unknown', 'Yes')
RISK_NUMSUB_CHOICES = ('', 'One', 'Two or more')
RISK_PENALTY_CHOICES= ('', 'Low', 'Medium', 'High')
RISK_WEAPONS_CHOICES=('', 'No', 'Unknown', 'Yes')
RISK_LANGUAGE_CHOICES=('', 'No', 'Unknown', 'Yes')
RISK_HISTLAWAVER_CHOICES=('', 'No', 'Unknown', 'Yes')
TRAINING_CHOICES=('', 'Yes', 'No')


class Trip(models.Model):
    # Officer
    officer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gavia_num = models.PositiveIntegerField(null=True, blank=True)
    # Enforcement record
    purpose = models.CharField(max_length=120, choices=[(d, d) for d in PURPOSES])
    purpose_other = models.CharField(max_length=255, blank=True, default='')
    start_date_planned = models.DateTimeField(blank=True)
    end_date_planned = models.DateTimeField(blank=True)
    legislation = models.CharField(max_length=20, choices=[(d, d) for d in LEGS])
    reg1 = models.CharField(max_length=60, blank=True, default='', choices=[(d, d) for d in REGS])
    reg2 = models.CharField(max_length=60, blank=True, default='', choices=[(d, d) for d in REGS])
    reg3 = models.CharField(max_length=60, blank=True, default='', choices=[(d, d) for d in REGS])
    partner1 = models.CharField(max_length=20, choices=[(d, d) for d in PARTNERS], blank=True, default='')
    partner2 = models.CharField(max_length=20, choices=[(d, d) for d in PARTNERS], blank=True, default='')
    intelreport = models.CharField(max_length=10, choices=[(d, d) for d in INTEL_REPORT])
    intelreport_name = models.CharField(max_length=200, blank=True, default='')
    # Destination
    dest_name = models.CharField(max_length=200)
    dest_address = models.CharField(max_length=255, blank=True, default='')
    dest_province = models.CharField(max_length=100, blank=True, default='')
    dest_city = models.CharField(max_length=100, blank=True, default='')
    dest_postal_code = models.CharField(max_length=100, blank=True, default='')
    dest_lat = models.FloatField(null=True, blank=True)
    dest_lng = models.FloatField(null=True, blank=True)
    
    # Risks considerations
    risk_loc = models.CharField(max_length=50, choices=[(d, d) for d in RISK_LOCATIONS])
    risk_loc_val = models.IntegerField()
    risk_loc_fam = models.CharField(max_length=50, choices=[(d, d) for d in RISK_LOC_FAM])
    risk_loc_fam_val = models.IntegerField()
    risk_time = models.CharField(max_length=50, choices=[(d, d) for d in RISK_TIME_CHOICES])
    risk_time_val = models.IntegerField()
    risk_weather = models.CharField(max_length=50, choices=[(d, d) for d in RISK_WEATHER_CHOICES])
    risk_weather_val = models.IntegerField()
    risk_terrain = models.CharField(max_length=50, choices=[(d, d) for d in RISK_TERRAIN_CHOICES])
    risk_terrain_val = models.IntegerField()
    risk_comm = models.CharField(max_length=50, choices=[(d, d) for d in RISK_COMM_CHOICES])
    risk_comm_val = models.IntegerField()
    risk_emergency = models.CharField(max_length=50, choices=[(d, d) for d in RISK_EMERGENCY_CHOICES])
    risk_emergency_val = models.IntegerField()
    risk_distance = models.CharField(max_length=50, choices=[(d, d) for d in RISK_DISTANCE_CHOICES])
    risk_distance_val = models.IntegerField()
    risk_transport = models.CharField(max_length=50, choices=[(d, d) for d in RISK_TRANSPORT_CHOICES])
    risk_transport_val = models.IntegerField()
    risk_criminal = models.CharField(max_length=50, choices=[(d, d) for d in RISK_CRIMINAL_CHOICES])
    risk_criminal_val = models.IntegerField()
    risk_compliance = models.CharField(max_length=50, choices=[(d, d) for d in RISK_COMPLIANCE_CHOICES])
    risk_compliance_val = models.IntegerField()
    risk_numsub = models.CharField(max_length=50, choices=[(d, d) for d in RISK_NUMSUB_CHOICES])
    risk_numsub_val = models.IntegerField()
    risk_penalty = models.CharField(max_length=50, choices=[(d, d) for d in RISK_PENALTY_CHOICES])
    risk_penalty_val = models.IntegerField()
    risk_weapons = models.CharField(max_length=50, choices=[(d, d) for d in RISK_WEAPONS_CHOICES])
    risk_weapons_val = models.IntegerField()
    risk_language = models.CharField(max_length=50, choices=[(d, d) for d in RISK_LANGUAGE_CHOICES])
    risk_language_val = models.IntegerField()
    risk_histlawaver = models.CharField(max_length=50, choices=[(d, d) for d in RISK_HISTLAWAVER_CHOICES])
    risk_histlawaver_val = models.IntegerField()
    risk_sum = models.IntegerField()
    risk_score_label = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    # date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")

    class Meta:
        db_table = 'trips'

    def __str__(self):
        return self.firstname + " " +  self.lastname + ", " + self.purpose + ", " + self.dest_city + ", " + self.risk_score_label + ", " + str(self.date_created.strftime("%Y-%m-%d"))

    # We use this for redirect (reverse) and let the view handle the redirect with the returned string
    # Redirects after Create new
    def get_absolute_url(self):
        return reverse('trip-detail', kwargs={'pk': self.pk})

class Hoir(models.Model):
    # Officer
    officer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    trip_id = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    # Occurence - injury
    injury = models.BooleanField()
    no_injury = models.BooleanField()
    incident = models.BooleanField()
    motor_vehicle = models.BooleanField()
    serious_accident = models.BooleanField()
    emerg_procedure = models.BooleanField()
    loss_consc = models.BooleanField()
    explosion = models.BooleanField()
    other_inj = models.CharField(max_length=255, blank=True)
    first_aid = models.BooleanField()
    minor_injury = models.BooleanField()
    disabling_injury = models.BooleanField()
    # Employee
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    occupation = models.CharField(max_length=30)
    years_experience = models.IntegerField()
    work_address = models.CharField(max_length=255)
    region = models.CharField(max_length=100)
    branch = models.CharField(max_length=50, default="Enforcement branch")
    status = models.CharField(max_length=100)
    duties = models.CharField(max_length=10)
    shift_hours = models.CharField(max_length=10)
    date_reported = models.DateField(blank=True)
    days_lost = models.CharField(max_length=10)
    training_given = models.CharField(max_length=10, choices=[(t, t) for t in TRAINING_CHOICES])
    training_given_specify = models.CharField(max_length=200, blank=True)
    tha_swp = models.CharField(max_length=10, choices=[(t, t) for t in TRAINING_CHOICES])
    tha_swp_specify = models.CharField(max_length=200, blank=True)
    injury_description = models.TextField()
    injury_causes = models.TextField()
    # Employer
    mail_address = models.CharField(max_length=255)
    supervisor = models.CharField(max_length=50)
    supervisor_phone = models.CharField(max_length=20)
    witnesses = models.TextField()
    # Occurence
    location = models.CharField(max_length=150)
    weather = models.CharField(max_length=100, blank=True)
    occurence_date_hazard = models.DateTimeField()
    occurence_description = models.TextField()
    occurence_causes = models.TextField()
    property_damage = models.TextField()

    class Meta:
        db_table = 'hoirs'

    def __str__(self):
        return self.firstname + " " +  self.lastname + ", " + str(self.date_created.strftime("%Y-%m-%d"))

    def get_absolute_url(self):
        return reverse('hoir-detail', kwargs={'pk': self.pk})

class Oscr(models.Model):
    # Officer
    officer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    trip_id = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    # Type of risk
    verbal_threat = models.BooleanField(blank=True)
    weapons_nearby = models.BooleanField(blank=True)
    physical_contact = models.BooleanField(blank=True)
    assault = models.BooleanField(blank=True)
    damage_equipment = models.BooleanField(blank=True)
    other_risk_specify = models.TextField(blank=True, max_length=200)
    # Location risk encountered
    industrial_facility = models.BooleanField(blank=True)
    commercial_facility = models.BooleanField(blank=True)
    remote_location = models.BooleanField(blank=True)
    agriculture = models.BooleanField(blank=True)
    marine = models.BooleanField(blank=True)
    first_nations = models.BooleanField(blank=True)
    isolated = models.BooleanField(blank=True)
    other_riskloc_specify = models.TextField(blank=True, max_length=200)
    # Duties
    inspections = models.BooleanField(blank=True)
    witness_statements = models.BooleanField(blank=True)
    court_docs = models.BooleanField(blank=True)
    warrant = models.BooleanField(blank=True)
    surveillance = models.BooleanField(blank=True)
    other_duty_specify =models.TextField(blank=True, max_length=200)
    # Regulations
    fisheries_act = models.BooleanField(blank=True)
    name_reg1 = models.TextField(blank=True, max_length=200)
    cepa_1999 = models.BooleanField(blank=True)
    name_reg2 = models.TextField(blank=True, max_length=200)
    # Employee
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    years_experience = models.IntegerField()
    region = models.CharField(max_length=100)
    branch = models.CharField(max_length=50, default="Enforcement branch")
    gavia_num = models.PositiveIntegerField(null=True, blank=True)
    # Occurence
    location = models.CharField(max_length=150)
    occurence_date_hazard = models.DateTimeField()
    occurence_description = models.TextField(max_length=800)

    class Meta:
        db_table = 'oscrs'

    def __str__(self):
        return self.firstname + " " +  self.lastname + ", " + str(self.date_created.strftime("%Y-%m-%d"))

    def get_absolute_url(self):
        return reverse('oscr-detail', kwargs={'pk': self.pk})

class Closeout(models.Model):
    officer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    trip_id = models.CharField(max_length=200, blank=True)
    close_remarks = models.TextField(max_length=800)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'closeouts'

    def __str__(self):
        return str(self.date_created.strftime("%Y-%m-%d"))

    def get_absolute_url(self):
        return reverse('closeout-detail', kwargs={'pk': self.pk})

class Office(models.Model):
    region = models.CharField(max_length=200)
    city = models.CharField(max_length=75)
    address = models.CharField(max_length=255)
    province = models.CharField(max_length=75)
    postal_code = models.CharField(max_length=75)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    point = models.PointField(null=True, blank=True)

    class Meta:
        db_table = 'offices'
