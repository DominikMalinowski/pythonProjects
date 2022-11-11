# Cats inventory advanced manager v3 (with for and if)
print("Starting program")

print("Preparing data")
cat1 = "Kitty"
cat2 = "Pussy"
cat3 = "Paw"
missing_cat = 'Pussy'

print("Initialising cats list")
cats = [cat1, cat2, cat3]

print("Returning cats")
for cat in cats:
   if cat is missing_cat:
      print(f'Below cat is reported as missing')
   print(f"Found cat: {cat}")
print("Cat program finished")