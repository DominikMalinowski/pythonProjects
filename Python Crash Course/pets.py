pets = ["pies", "kot", "pies", "złota rybka", "kot", "królik", "kot"]
print(pets)

while "kot" in pets:
    pets.remove("kot")

def describe_pet(animal_type='pies', pet_name): 
    """Wyświetla informacjie o zwierzeciu"""
    print(f"\nMoje zwierzę to {animal_type}, a nazwa się {pet_name.title()}.")

describe_pet(animal_type='pies', pet_name='harry')