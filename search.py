# search.py
import sys
from BTrees.OOBTree import OOBTree

from utils import get_root
from models import Country, Region, Airport  # pas obligatoire, mais propre


def ensure_btrees(root):
    if not hasattr(root, "countries"):
        root.countries = OOBTree()
    if not hasattr(root, "regions"):
        root.regions = OOBTree()
    if not hasattr(root, "airports"):
        root.airports = OOBTree()


# Recherche un pays par son code, ex : "FR", "GB".
# Retourne l'objet Country ou None si introuvable.
def search_country(root, code: str) -> Country | None:
    return root.countries.get(code)

# Recherche une région par son code, ex : "FR-IDF", "GB-ENG".
def search_region(root, code: str) -> Region | None:
    return root.regions.get(code)


# Recherche un airport par son identifiant, ex : "LFPG", "LFPB", "EGLL".
def search_airport(root, ident: str) -> Airport | None:
    return root.airports.get(ident)


# On attend au moins 2 arguments :
# 1) le type de recherche : country / region / airport
# 2) le code ou identifiant à chercher
def main():

    if len(sys.argv) < 3:
        print("Usage : python search.py <type> <code>")
        print("Types possibles :")
        print("  country <code_pays>   ex : country FR")
        print("  region  <code_region> ex : region FR-IDF")
        print("  airport <ident>       ex : airport LFPG")
        sys.exit(1)

    search_type = sys.argv[1]  # "country" / "region" / "airport"
    code = sys.argv[2]         # "FR", "FR-IDF", "LFPG", etc.

    # 1. On récupère la racine de la base
    root = get_root()

    # 2. On s'assure que les BTrees existent
    ensure_btrees(root)

    # 3. On fait la recherche selon le type demandé
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
            # On affiche un peu plus d’infos, y compris pays et région
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
