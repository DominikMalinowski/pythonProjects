# Cats inventory advanced manager v4 (with for and if and function)
print("Starting program")

print("Preparing data")
cat1 = "Kitty"
cat2 = "Pussy"
cat3 = "Paw"

print("Initialising cats list")
cats = [cat1, cat2, cat3]

def is_missing(cat_to_check):
    missing_cat = "Pussy"
    if cat_to_check is missing_cat:
        print(f"Cat in line below reported as missing!")

print("Returning cats")

for cat in cats:
   is_missing(cat)
   print(f"Found cat: {cat}")

print("Cat program finished")

