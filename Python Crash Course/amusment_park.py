age= 2
if age <4:
    print("Masz wejście za darmo")
elif age<18:
    print("Wejście za 25pln")
else:
    print("Wejście za 50pln") 

age = 67
if age < 5:
    price=0
elif age <18:
    price=10
else:
    price=20

print(f"Cena biletu wynosi {price} pln.")
