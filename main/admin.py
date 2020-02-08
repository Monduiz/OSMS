from django.contrib import admin
from .models import Trip, Hoir, Oscr, Closeout, Office


class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'officer', 'firstname', 'lastname', 'purpose', 'legislation', 'dest_name', 'dest_city', 'risk_score_label', 'date_created')
    search_fields = ('purpose', 'dest_name')
    readonly_fields = ('id', 'date_created',)

    # These are required
    filter_horizontal = ()
    list_filter = ()
    fieldsets =()

class HoirAdmin(admin.ModelAdmin):
    list_display = ('id', 'officer', 'firstname', 'lastname', 'date_created')
    search_fields = ('occurence_description', 'occurence_causes')
    readonly_fields = ('id', 'date_created',)

    # These are required
    filter_horizontal = ()
    list_filter = ()
    fieldsets =()

class OscrAdmin(admin.ModelAdmin):
    list_display = ('id', 'officer', 'firstname', 'lastname', 'date_created')
    search_fields = ('occurence_description', 'occurence_causes')
    readonly_fields = ('id', 'date_created',)

    # These are required
    filter_horizontal = ()
    list_filter = ()
    fieldsets =()

class CloseoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'officer', 'date_created')
    readonly_fields = ('id', 'date_created',)

    # These are required
    filter_horizontal = ()
    list_filter = ()
    fieldsets =()

class OfficeAdmin(admin.ModelAdmin):
    list_display = ('region', 'address', 'city', 'province', 'postal_code')

    # These are required
    filter_horizontal = ()
    list_filter = ()
    fieldsets =()

admin.site.register(Trip, TripAdmin)
admin.site.register(Hoir, HoirAdmin)
admin.site.register(Oscr, OscrAdmin)
admin.site.register(Closeout, CloseoutAdmin)
admin.site.register(Office, OfficeAdmin)
