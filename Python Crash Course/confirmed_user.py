#tworzymy listę osób do zweryfikowania 
#tworzymy listę do już zweryfikowanych 
unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
confirmed_users = []

#weryfikujemy poszczególnych użytkowników, aż lista będzie pusta 
#kazdego zweryfikowane użytkownika przenosimy na liste już zweryfikowanych 
while unconfirmed_users: 
    current_users = unconfirmed_users.pop()

    print(f"Weryfikacja użytkownika: {current_users.title()}")
    confirmed_users.append(current_users)

#wyświetlenie zweryfikowanych użytkowników 
print(f"\n Zweryfikowano wymienionych ponizej użytkowników: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())