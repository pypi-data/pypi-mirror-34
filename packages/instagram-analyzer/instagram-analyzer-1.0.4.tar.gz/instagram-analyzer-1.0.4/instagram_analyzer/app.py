import requests
import json
import os.path
import time
from typing import NoReturn
from beautifultable import BeautifulTable

# URIs

INSTA_MEDIA_URI: str = 'https://api.instagram.com/v1/users/self/media/recent'
LOCATION_IQ_URI: str = 'https://us1.locationiq.org/v1/reverse.php'

# Files

INSTA_MEDIA_JSON_FILE_NAME = './insta_media_data.json'
INSTA_LOCATIONS_JSON_FILE_NAME = './insta_locations_data.json'
INSTA_COUNTRIES_JSON_FILE_NAME = './insta_countries_data.json'
INSTA_CITIES_JSON_FILE_NAME = './insta_cities_data.json'


class InstaAnalyzer(object):

    def __init__(self, insta_token: str, location_iq_token: str = None):
        self._insta_token = insta_token
        self._location_iq_token = location_iq_token

        self._read_media_from_file: bool = False

        self._insta_media_data: dict = None
        self._locations: dict = {}
        self._countries: dict = {}
        self._cities: dict = {}

    @property
    def insta_token(self):
        return self._insta_token

    @insta_token.setter
    def insta_token(self, value):
        self._insta_token = value

    @property
    def location_iq_token(self):
        return self._location_iq_token

    @location_iq_token.setter
    def location_iq_token(self, value):
        self._location_iq_token = value

    @property
    def read_media_from_file(self):
        return self._read_media_from_file

    @read_media_from_file.setter
    def read_media_from_file(self, value):
        self._read_media_from_file = value

    @property
    def insta_media_data(self):
        return self._insta_media_data

    @property
    def locations(self):
        return self._locations

    @property
    def countries(self):
        return self._countries

    @property
    def cities(self):
        return self._cities

    def load_instagram_media(self):
        """Load Instagram media. If read_media_from_file is set to true, media is loaded from file"""

        if self._read_media_from_file:
            self._insta_media_data = read_insta_media()
        else:
            if self._insta_token is None:
                raise ValueError("Insta token must be present, set insta_token")

            self._insta_media_data = load_insta_media(self._insta_token)
            store_insta_media(self._insta_media_data)

    def analyze_locations(self):
        """Analyze location data, Instagram media should be loaded first"""

        if self._insta_media_data is None:
            raise ValueError("Insta media is not yet loaded, make sure to call load_instagram_media before")

        location_analysis: dict = analyze_locations(self._insta_media_data, self._location_iq_token)
        self._countries = location_analysis['countries']
        self._locations = location_analysis['locations']
        self._cities = location_analysis['cities']

    def print_locations(self):
        """Print location data analysis"""

        print_locations_data(self._locations, self._countries, self._cities)

    def run(self):
        """Load Instagram media and save it to file. Analyze locations data and store it to file.
        Print location analysis result at the end """
        self.load_instagram_media()
        self.analyze_locations()
        self.print_locations()


def load_insta_media(insta_token: str) -> dict:
    print('Loading Instagram media [', end='', flush=True)

    next_max_id: str = None
    next_page: bool = True

    all_media: dict = {}

    with requests.Session() as session:
        while next_page:
            media = get_recent_media(session=session, insta_token=insta_token, next_max_id=next_max_id)
            next_max_id = media['next_max_id']
            next_page = media['next_page']
            all_media.update(media['media'])
            print("#", end="", flush=True)

    print('] [DONE] - Media items size: ', len(all_media))

    return all_media


def read_insta_media() -> dict:
    if not os.path.isfile(INSTA_MEDIA_JSON_FILE_NAME):
        raise ValueError("Media has not yet been loaded, file: " + INSTA_MEDIA_JSON_FILE_NAME + " does not exist")

    with open(INSTA_MEDIA_JSON_FILE_NAME) as f:
        return json.loads(f.read())


def store_insta_media(insta_media_data: dict = None) -> NoReturn:
    print('Saving media data to file ', end='', flush=True)
    with open(INSTA_MEDIA_JSON_FILE_NAME, "wb") as f:
        f.write(json.dumps(insta_media_data).encode("utf-8"))
    print('[DONE]')


def get_recent_media(session: requests.Session, insta_token: str, next_max_id: str = None) -> dict:
    # set count to 2000 to get max data per request
    payload: dict = {
        'access_token': insta_token,
        'max_id': next_max_id,
        'count': 2000
    }

    try:
        response = session.get(INSTA_MEDIA_URI, params=payload)
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        raise ValueError('HTTP error calling Instagram API') from e

    except requests.exceptions.RequestException as e:
        raise ValueError('Connection error calling Instagram API') from e

    json_response: dict = response.json()

    if 'code' in json_response and json_response['code'] != 200:
        raise ValueError('Error while calling Instagram API, error_type: '
                         + json_response['error_type'] + ', message: '
                         + json_response['error_message'])

    media: dict = {}
    for item in json_response['data']:
        media[item['id']] = item

    next_max_id = json_response['pagination'].get('next_max_id', None)

    return {'next_max_id': next_max_id, 'next_page': next_max_id is not None, 'media': media}


def analyze_locations(insta_media_data: dict, location_iq_token: str) -> dict:
    print('Analyzing locations ...')

    locations: dict = extract_locations_from_media(insta_media_data)
    countries: dict = {}
    cities: dict = {}

    fill_additional_location_data(locations, cities, countries, location_iq_token)
    store_locations_data(locations, countries, cities)

    return {'locations': locations, 'countries': countries, 'cities': cities}


def fill_additional_location_data(locations: dict, cities: dict, countries: dict, location_iq_token: str) -> NoReturn:
    """Fill additional location data using LocationIQ API.

    Append additional data to locations, fill cities and countries.
    """

    if location_iq_token is None:
        print('Skipping additional location data loading, LocationIQ token not set')
    else:
        print('Loading additional location data (should take about', len(locations), 'seconds) [', end='', flush=True)
        with requests.Session() as session:
            for key in locations:
                location = locations[key]
                media_items = location['media_items']

                # Load additional data
                additional_location_data = load_additional_location_data(
                    session=session,
                    location=location,
                    location_iq_token=location_iq_token)

                # Extract additional data
                country = additional_location_data['address']['country']

                if 'city' in additional_location_data['address']:
                    city = additional_location_data['address']['city']
                elif 'town' in additional_location_data['address']:
                    city = additional_location_data['address']['town']
                elif 'village' in additional_location_data['address']:
                    city = additional_location_data['address']['village']
                else:
                    city = 'Other'

                location['additional_data'] = additional_location_data

                # Fill countries
                if country in countries:
                    countries[country]['count'] += 1
                    countries[country]['media_items'] += media_items
                else:
                    countries[country] = {
                        'count': 1,
                        'media_items': [media_items]
                    }

                # Fill cities
                if city in cities:
                    cities[city]['count'] += 1
                    cities[city]['media_items'] += media_items
                else:
                    cities[city] = {'count': 1, 'media_items': [media_items]}

                # LocationIQ rate limit (1 request per second)
                print("#", end="", flush=True)
                time.sleep(1)

        print('] [DONE]')


def extract_locations_from_media(insta_media_data: dict) -> dict:
    locations: dict = {}

    for key in insta_media_data.keys():
        media_item = insta_media_data[key]
        location = media_item['location']

        if location is not None:
            location_id = location['id']
            if location_id in locations:
                locations[location_id]['count'] += 1
                locations[location_id]['media_items'].append(
                    {
                        'id': media_item['id'],
                        'image': media_item['images']['standard_resolution']['url'],
                        'link': media_item['link']
                    }
                )
            else:
                location['count'] = 1
                location['media_items'] = [
                    {
                        'id': media_item['id'],
                        'image': media_item['images']['standard_resolution']['url'],
                        'link': media_item['link']
                    }
                ]
                locations[location_id] = location

    return locations


def store_locations_data(locations, countries, cities) -> NoReturn:
    print('Saving location data to files ', end='', flush=True)

    with open(INSTA_LOCATIONS_JSON_FILE_NAME, "wb") as f:
        f.write(json.dumps(locations).encode("utf-8"))

    with open(INSTA_COUNTRIES_JSON_FILE_NAME, "wb") as f:
        f.write(json.dumps(countries).encode("utf-8"))

    with open(INSTA_CITIES_JSON_FILE_NAME, "wb") as f:
        f.write(json.dumps(cities).encode("utf-8"))

    print('[DONE]')


def print_locations_data(locations, countries, cities) -> NoReturn:
    # Sort by occurrences
    sorted_locations = sorted(locations.items(), key=lambda i: i[1]['count'], reverse=True)
    sorted_countries = sorted(countries.items(), key=lambda i: i[1]['count'], reverse=True)
    sorted_cities = sorted(cities.items(), key=lambda i: i[1]['count'], reverse=True)

    print('You have visited', len(locations), 'different locations')
    print('You have visited', len(countries), 'different countries')
    print('You have visited', len(cities), 'different cities')

    # Pretty print locations
    print('\n Locations: \n')
    locations_table = BeautifulTable()
    locations_table.column_headers = ['rank', 'location', 'occurrences']
    locations_table.column_alignments['location'] = BeautifulTable.ALIGN_LEFT

    rank: int = 1
    for location in sorted_locations:
        locations_table.append_row([rank, location[1]['name'], location[1]['count']])
        rank += 1

    print(locations_table)

    # Pretty print countries
    print('\n Countries: \n')
    countries_table = BeautifulTable()
    countries_table.column_headers = ['rank', 'country', 'occurrences']
    countries_table.column_alignments['country'] = BeautifulTable.ALIGN_LEFT

    rank = 1
    for country in sorted_countries:
        countries_table.append_row([rank, country[0], country[1]['count']])
        rank += 1

    print(countries_table)

    # Pretty print cities
    print('\n Cities: \n')
    cities_table = BeautifulTable()
    cities_table.column_headers = ['rank', 'city', 'occurrences']
    cities_table.column_alignments['city'] = BeautifulTable.ALIGN_LEFT

    rank = 1
    for city in sorted_cities:
        cities_table.append_row([rank, city[0], city[1]['count']])
        rank += 1

    print(cities_table)


def load_additional_location_data(session: requests.Session, location: dict, location_iq_token: str) -> dict:
    payload: dict = {
        'key': location_iq_token,
        'lat': location['latitude'],
        'lon': location['longitude'],
        'format': 'json'
    }

    try:
        response = session.get(LOCATION_IQ_URI, params=payload)
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        raise ValueError('HTTP error calling LocationIQ API') from e

    except requests.exceptions.RequestException as e:
        raise ValueError('Connection error calling LocationIQ API') from e

    return response.json()


def main():
    analyzer = InstaAnalyzer(
        insta_token='48446217.1677ed0.5b1bf03ac66348a795b7556d2dbff211',
        location_iq_token='1e8ea0a390d8cd')
    analyzer.read_media_from_file = False
    analyzer.run()


if __name__ == '__main__':
    main()
