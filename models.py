from persistent import Persistent

class Country(Persistent):
    def __init__(self, name, code, continent, wikipedia_link, keywords):
        self.name = name
        self.code = code
        self.continent = continent
        self.wikipedia_link = wikipedia_link
        self.keywords = keywords

class Region(Persistent):
    def __init__(self, code, name, local_code,continent, iso_country, wikipedia_link, keywords):
        self.code = code
        self.name = name
        self.local_code = local_code
        self.continent = continent
        self.iso_country = iso_country
        self.wikipedia_link = wikipedia_link
        self.keywords = keywords


class Airport(Persistent):
    def __init__(self, ident, type, name, latitude_deg, longitude_deg, elevation_ft, continent, iso_country, iso_region, municipality, scheduled_service, icao_code, iata_code, gps_code, local_code, home_link, wikipedia_link, keywords, country: Country, region: Region):
        self.ident = ident
        self.type = type
        self.name = name
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.elevation_ft = elevation_ft
        self.continent = continent
        self.iso_country = iso_country
        self.iso_region = iso_region
        self.municipality = municipality
        self.scheduled_service = scheduled_service
        self.icao_code = icao_code
        self.iata_code = iata_code
        self.gps_code = gps_code
        self.local_code = local_code
        self.home_link = home_link
        self.wikipedia_link = wikipedia_link
        self.keywords = keywords
        self.country = country
        self.region = region