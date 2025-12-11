import csv
from BTrees.OOBTree import OOBTree
from utils import get_root
from models import Region, Country, Airport


def ensure_btrees(root):
    if not hasattr(root, "countries"):
        root.countries = OOBTree()
    if not hasattr(root, "regions"):
        root.regions = OOBTree()
    if not hasattr(root, "airports"):
        root.airports = OOBTree()

def import_data(root, filename: str):
    with open(filename, newline="", encoding="UTF-8") as f:
        reader = csv.DictReader(f)

        if "countries" in filename:
            btree: OOBTree = root.countries
            for row in reader:
                country = Country(
                    name=row["name"],
                    code=row["code"],
                    continent=row["continent"],
                    wikipedia_link=row["wikipedia_link"],
                    keywords=row["keywords"]
                )
                btree[country.code] = country

        elif "regions" in filename:
            btree: OOBTree = root.regions
            for row in reader:
                region = Region(
                    code=row["code"],
                    name=row["name"],
                    local_code=row["local_code"],
                    continent=row["continent"],
                    iso_country=row["iso_country"],
                    wikipedia_link=row["wikipedia_link"],
                    keywords=row["keywords"]
                )
                btree[region.code] = region

        elif "airports" in filename:
            btree: OOBTree = root.airports
            for row in reader:
                country = root.countries.get(row["iso_country"])
                region = root.regions.get(row["iso_region"])

                airport = Airport(
                    ident=row["ident"],
                    type=row["type"],
                    name=row["name"],
                    latitude_deg=float(row["latitude_deg"]) if row["latitude_deg"] else None,
                    longitude_deg=float(row["longitude_deg"]) if row["longitude_deg"] else None,
                    elevation_ft=int(row["elevation_ft"]) if row["elevation_ft"] else None,
                    continent=row["continent"],
                    iso_country=row["iso_country"],
                    iso_region=row["iso_region"],
                    municipality=row["municipality"],
                    scheduled_service=row["scheduled_service"],
                    icao_code=row["icao_code"],
                    iata_code=row["iata_code"],
                    gps_code=row["gps_code"],
                    local_code=row["local_code"],
                    home_link=row["home_link"],
                    wikipedia_link=row["wikipedia_link"],
                    keywords=row["keywords"],
                    country=country,
                    region=region
                )
                btree[airport.ident] = airport
        else:
            print("Unknown file type.")
            return
