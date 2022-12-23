#zadanie 5.8
uzytkownicy=["adam","karolina","daria","admin","robert"] 
for uzytkownik in uzytkownicy:
    if uzytkownik != "admin":
        print(f"Witaj {uzytkownik.title()}")
    else:
        print("Ave Cezar, czy majestat zechce wysłuchać raportu Kalcjusza Maximusa Longinusa")

#zadanie 5.9
#uzytkownicy=["adam","karolina","daria","admin","robert"]
uzytkownicy=[]
if uzytkownicy:
    for uzytkownik in uzytkownicy:  
        if uzytkownik != "admin":
            print(f"Witaj {uzytkownik.title()}")
        else:
            print("Ave Cezar, czy majestat zechce wysłuchać raportu Kalcjusza Maximusa Longinusa")
else:
    print("Potrzebujemy więcej ludzi\n")

#zadanie 5.10
current_users = ["masturbator9000","TWOJA STARA","xyz","ksiadz_robak","jezus hitler"]
new_users=["twoja stara","adolf chrystus","abc","jacek_soplica","bóg_patrzy_jak_sie_masturbujesz"]

for new_user in new_users:
    for current_user in current_users:
        if new_user.lower()==current_user.lower():
            print(f"Ty złodzieju '{new_user}' jest zajęty")
    else: 
        print(f"Możesz użyć '{new_user}' jako nazwy użytkownika")
        
#zadanie 5.11
liczby=list(range(1,10))
for liczba in liczby:
    if liczba == 1:
        print("1st")
    elif liczba == 2:
        print("2nd")
    elif liczba == 3:
        print("3rd")
    else:
        print(f"{liczba}th")