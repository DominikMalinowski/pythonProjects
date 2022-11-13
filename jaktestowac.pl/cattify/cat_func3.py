# Cats inventory advanced manager v5 (with for and if and function external)

from cats_helpers import is_missing

print("Starting program")

print("Preparing data")
cat1 = "Kitty"
cat2 = "Pussy"
cat3 = "Paw"

print("Initialising cats list")
cats = [cat1, cat2, cat3]

print("Returning cats")

def cat_printer(cat_list):
    for cat in cat_list:
        is_missing(cat)
        print(f"Found cat: {cat}")

print("Cat program finished")

cat_printer(cats)