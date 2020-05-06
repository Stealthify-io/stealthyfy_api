import googlemaps
import time

key = "AIzaSyAbybEMQeWDCq0lOnf26atmD1Af3L5nK9Q"


def get_places(lat, lng):
    gmaps = googlemaps.Client(key=key)
    print(gmaps)
    location = (lat, lng)
    print(location)
    all_results = dict({})

    x = gmaps.places_nearby(type="store", location=location, rank_by='distance')
    grocery_results = x['results']
    print(x)

	
    while 'next_page_token' in x:
        time.sleep(1)
        try:
            x = gmaps.places_nearby(page_token=x['next_page_token'])
            grocery_results += x['results']
        except:
            pass

    all_results["store"] = grocery_results

    x = gmaps.places_nearby(type="Walmart", location=location, rank_by='distance')
    walmart_results = x['results']

    while 'next_page_token' in x:
        time.sleep(1)
        try:
            x = gmaps.places_nearby(page_token=x['next_page_token'])
            walmart_results += x['results']
        except:
            pass

    all_results["walmart"] = walmart_results

    x = gmaps.places_nearby(type="pharmacy", location=location, rank_by='distance')
    pharmacy_results = x['results']

    while 'next_page_token' in x:
        time.sleep(1)
        try:
            x = gmaps.places_nearby(page_token=x['next_page_token'])
            pharmacy_results += x['results']
        except:
            pass

    all_results["pharmacy"] = pharmacy_results
    
    return all_results
