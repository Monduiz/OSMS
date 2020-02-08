from main.models import Trip, Office
#from django.contrib.gis.geos import Point
from geojson import Feature, Point, FeatureCollection, dump

# queries
offices = Office.objects.all().order_by('city')
trips = Trip.objects.all().order_by('id')

# Creates choices for workplace addresses and regions from a table in the database.
def create_work_addr():
    work_addr = []
    for office in offices:
        officeObject = {'region': office.region,
                        'address': office.region + ": " + office.address + ", " + office.city + ", " + office.province + ", " + office.postal_code}

        #officeObject = {"Region: "+ office.region + ", " + office.address + ", " + office.city + ", " + office.province + ", " + office.postal_code}
        work_addr.append(officeObject)

    return work_addr

def create_trip_link():
    trip_links = []
    for trip in trips:
        tripObject = {'id': trip.id, 'trip_description': trip.dest_name + ", " +
                    trip.dest_city + ", " + trip.start_date_planned.strftime("%Y-%m-%d")}

        trip_links.append(tripObject)
    return trip_links

def create_loc():
    locations = []
    for loc in offices:
        point = Point(loc.point)
        properties= {
            'title': loc.region,
            'city': loc.city,
            'address': loc.address,
            'province': loc.province,
            'postal_code': loc.postal_code}

        feat_point = Feature(geometry=point, properties=properties)
        locations.append(feat_point)
    return locations


def create_trip_loc(x):
    locations = []
    for loc in x:
        point = Point([loc.dest_lng, loc.dest_lat])
        properties= {
            'title': loc.dest_name,
            'city': loc.dest_city,
            'address': loc.dest_address,
            'province': loc.dest_province,
            'postal_code': loc.dest_postal_code}

        feat_point = Feature(geometry=point, properties=properties)
        locations.append(feat_point)
    return locations
