# Generated by Django 2.2.5 on 2020-01-24 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=400)),
                ('province', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=30)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'offices',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('gavia_num', models.PositiveIntegerField(blank=True, null=True)),
                ('purpose', models.CharField(choices=[('', ''), ('Planned inspection', 'Planned inspection'), ('Unplanned inspection', 'Unplanned inspection'), ('Surveillance', 'Surveillance'), ('Production order', 'Production order'), ('Serving court documents', 'Serving court documents'), ('Enforcement action', 'Enforcement action'), ('Undercover operation', 'Undercover operation'), ('General warrant', 'General warrant'), ('Warrant', 'Warrant'), ('Interview', 'Interview'), ('Other', 'Other')], max_length=120)),
                ('purpose_other', models.CharField(blank=True, default='', max_length=400)),
                ('start_date_planned', models.DateTimeField(blank=True)),
                ('end_date_planned', models.DateTimeField(blank=True)),
                ('legislation', models.CharField(choices=[('', ''), ('FA', 'FA'), ('CEPA', 'CEPA'), ('FA and CEPA', 'FA and CEPA')], max_length=20)),
                ('reg1', models.CharField(blank=True, choices=[('', ''), ('2BER', '2BER'), ('AMMRR', 'AMMRR'), ('BIGR', 'BIGR'), ('CAMRR', 'CAMRR')], default='', max_length=60)),
                ('reg2', models.CharField(blank=True, choices=[('', ''), ('2BER', '2BER'), ('AMMRR', 'AMMRR'), ('BIGR', 'BIGR'), ('CAMRR', 'CAMRR')], default='', max_length=60)),
                ('reg3', models.CharField(blank=True, choices=[('', ''), ('2BER', '2BER'), ('AMMRR', 'AMMRR'), ('BIGR', 'BIGR'), ('CAMRR', 'CAMRR')], default='', max_length=60)),
                ('partner1', models.CharField(blank=True, choices=[('', ''), ('CBSA', 'CBSA'), ('DFO', 'DFO'), ('International', 'International'), ('OGD', 'OGD'), ('Parks Canada', 'Parks Canada'), ('Provincial', 'Provincial'), ('RCMP', 'RCMP'), ('Territorial', 'Territorial'), ('USFWS', 'USFWS')], default='', max_length=20)),
                ('partner2', models.CharField(blank=True, choices=[('', ''), ('CBSA', 'CBSA'), ('DFO', 'DFO'), ('International', 'International'), ('OGD', 'OGD'), ('Parks Canada', 'Parks Canada'), ('Provincial', 'Provincial'), ('RCMP', 'RCMP'), ('Territorial', 'Territorial'), ('USFWS', 'USFWS')], default='', max_length=20)),
                ('intelreport', models.CharField(choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('intelreport_name', models.CharField(blank=True, default='', max_length=200)),
                ('dest_name', models.CharField(max_length=200)),
                ('dest_address', models.CharField(blank=True, default='', max_length=400)),
                ('dest_province', models.CharField(blank=True, default='', max_length=100)),
                ('dest_city', models.CharField(blank=True, default='', max_length=100)),
                ('dest_postal_code', models.CharField(blank=True, default='', max_length=100)),
                ('dest_lat', models.FloatField(blank=True, null=True)),
                ('dest_lng', models.FloatField(blank=True, null=True)),
                ('risk_loc', models.CharField(choices=[('', ''), ('Urban', 'Urban'), ('Rural', 'Rural'), ('Remote', 'Remote'), ('Isolated', 'Isolated'), ('Marine', 'Marine')], max_length=50)),
                ('risk_loc_val', models.IntegerField()),
                ('risk_loc_fam', models.CharField(choices=[('', ''), ('Known', 'Known'), ('Unfamiliar', 'Unfamiliar'), ('Unknown', 'Unknown'), ('Public area', 'Public area')], max_length=50)),
                ('risk_loc_fam_val', models.IntegerField()),
                ('risk_time', models.CharField(choices=[('', ''), ('Daytime (30 min after sunrise)', 'Daytime (30 min after sunrise)'), ('Dusk or Dawn', 'Dusk or Dawn'), ('Night (30 min after sunset)', 'Night (30 min after sunset)')], max_length=50)),
                ('risk_time_val', models.IntegerField()),
                ('risk_weather', models.CharField(choices=[('', ''), ('Clear', 'Clear'), ('Mildly inclement', 'Mildly inclement'), ('Severely inclement', 'Severely inclement'), ('Unknown', 'Unknown')], max_length=50)),
                ('risk_weather_val', models.IntegerField()),
                ('risk_terrain', models.CharField(choices=[('', ''), ('Dry land', 'Dry land'), ('Mud / Wet lands', 'Mud / Wet lands'), ('Rivers / Lakes', 'Rivers / Lakes'), ('Ocean', 'Ocean'), ('Mountains', 'Mountains')], max_length=50)),
                ('risk_terrain_val', models.IntegerField()),
                ('risk_comm', models.CharField(choices=[('', ''), ('Cell / PTT/ Radio', 'Cell / PTT/ Radio'), ('Satelite', 'Satelite'), ('No comms', 'No comms')], max_length=50)),
                ('risk_comm_val', models.IntegerField()),
                ('risk_emergency', models.CharField(choices=[('', ''), ('Fast (<15 mins)', 'Fast (<15 mins)'), ('Medium (15-30 mins)', 'Medium (15-30 mins)'), ('Slow (>30 mins)', 'Slow (>30 mins)')], max_length=50)),
                ('risk_emergency_val', models.IntegerField()),
                ('risk_distance', models.CharField(choices=[('', ''), ('Close', 'Close'), ('Medium', 'Medium'), ('Far', 'Far')], max_length=50)),
                ('risk_distance_val', models.IntegerField()),
                ('risk_transport', models.CharField(choices=[('', ''), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=50)),
                ('risk_transport_val', models.IntegerField()),
                ('risk_criminal', models.CharField(choices=[('', ''), ('No', 'No'), ('Corporate', 'Corporate'), ('Violent', 'Violent')], max_length=50)),
                ('risk_criminal_val', models.IntegerField()),
                ('risk_compliance', models.CharField(choices=[('', ''), ('No', 'No'), ('Unknown', 'Unknown'), ('Yes', 'Yes')], max_length=50)),
                ('risk_compliance_val', models.IntegerField()),
                ('risk_numsub', models.CharField(choices=[('', ''), ('One', 'One'), ('Two or more', 'Two or more')], max_length=50)),
                ('risk_numsub_val', models.IntegerField()),
                ('risk_penalty', models.CharField(choices=[('', ''), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=50)),
                ('risk_penalty_val', models.IntegerField()),
                ('risk_weapons', models.CharField(choices=[('', ''), ('No', 'No'), ('Unknown', 'Unknown'), ('Yes', 'Yes')], max_length=50)),
                ('risk_weapons_val', models.IntegerField()),
                ('risk_language', models.CharField(choices=[('', ''), ('No', 'No'), ('Unknown', 'Unknown'), ('Yes', 'Yes')], max_length=50)),
                ('risk_language_val', models.IntegerField()),
                ('risk_histlawaver', models.CharField(choices=[('', ''), ('No', 'No'), ('Unknown', 'Unknown'), ('Yes', 'Yes')], max_length=50)),
                ('risk_histlawaver_val', models.IntegerField()),
                ('risk_sum', models.IntegerField()),
                ('risk_score_label', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'trips',
            },
        ),
        migrations.CreateModel(
            name='Hoir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('injury', models.BooleanField()),
                ('no_injury', models.BooleanField()),
                ('incident', models.BooleanField()),
                ('motor_vehicle', models.BooleanField()),
                ('serious_accident', models.BooleanField()),
                ('emerg_procedure', models.BooleanField()),
                ('loss_consc', models.BooleanField()),
                ('explosion', models.BooleanField()),
                ('other_inj', models.CharField(max_length=400)),
                ('first_aid', models.BooleanField()),
                ('minor_injury', models.BooleanField()),
                ('disabling_injury', models.BooleanField()),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(max_length=30)),
                ('years_experience', models.IntegerField()),
                ('work_address', models.CharField(max_length=400)),
                ('region', models.CharField(max_length=100)),
                ('branch', models.CharField(default='Enforcement', max_length=50)),
                ('status', models.CharField(max_length=100)),
                ('duties', models.CharField(max_length=10)),
                ('shift_hours', models.CharField(max_length=10)),
                ('date_reported', models.DateTimeField(blank=True)),
                ('days_lost', models.CharField(max_length=10)),
                ('training_given', models.CharField(choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('training_given_specify', models.CharField(max_length=200)),
                ('tha_swp', models.CharField(choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('tha_swp_specify', models.CharField(max_length=200)),
                ('injury_description', models.TextField()),
                ('injury_causes', models.TextField()),
                ('mail_address', models.CharField(max_length=400)),
                ('supervisor', models.CharField(max_length=50)),
                ('supervisor_phone', models.CharField(max_length=20)),
                ('witnesses', models.TextField()),
                ('location', models.CharField(max_length=150)),
                ('weather', models.CharField(blank=True, max_length=100)),
                ('occurence_date_hazard', models.DateTimeField(blank=True)),
                ('occurence_description', models.TextField()),
                ('occurence_causes', models.TextField()),
                ('property_damage', models.TextField()),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hoirs',
            },
        ),
    ]
