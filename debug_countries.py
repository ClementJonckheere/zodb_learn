# debug_countries.py
from BTrees.OOBTree import OOBTree
from utils import get_root

def ensure_btrees(root):
    if not hasattr(root, "countries"):
        root.countries = OOBTree()

root = get_root()
ensure_btrees(root)

print("Nb de pays en base :", len(root.countries))
print("Quelques clés :", list(root.countries.keys())[:10])
