# search.py
import sys
from BTrees.OOBTree import OOBTree

from utils import get_root
from models import Country, Region, Airport


def ensure_btrees(root):
    if not hasattr(root, "countries"):
        root.countries = OOBTree()
    if not hasattr(root, "regions"):
        root.regions = OOBTree()
    if not hasattr(root, "airports"):
        root.airports = OOBTree()

# Recherche un pay par son code
def search_country(root, code: str) -> Country | None:
    return root.countries.get(code)

# Recherche une region par son code
def search_region(root, code: str) -> Region | None:
    return root.regions.get(code)

# Recherche un aéroport par son identifiant
def search_airport(root, ident: str) -> Airport | None:
    return root.airports.get(ident)


def main():
    if len(sys.argv) < 3:
        sys.exit(1)

    search_type = sys.argv[1]  # "country" / "region" / "airport"
    code = sys.argv[2]         # "FR", "FR-IDF", "LFPG", etc.
    root = get_root()
    ensure_btrees(root)

    if search_type == "country":
        obj = search_country(root, code)
        if obj is None:
            print(f"Aucun pays trouvé pour le code '{code}'")
        else:
            print(f"Pays trouvé : {obj.code} - {obj.name}")

    elif search_type == "region":
        obj = search_region(root, code)
        if obj is None:
            print(f"Aucune région trouvée pour le code '{code}'")
        else:
            print(f"Région trouvée : {obj.code} - {obj.name}")

    elif search_type == "airport":
        obj = search_airport(root, code)
        if obj is None:
            print(f"Aucun aéroport trouvé pour l'identifiant '{code}'")
        else:
            # Plus d’infos, avec pays et région
            country = obj.country
            region = obj.region

            print(f"Aéroport : {obj.ident} - {obj.name}")
            if country:
                print(f"  Pays   : {country.code} - {country.name}")
            if region:
                print(f"  Région : {region.code} - {region.name}")

    else:
        print("Type inconnu. Utilise : country, region ou airport.")


if __name__ == "__main__":
    main()
