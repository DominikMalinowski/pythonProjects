# zadanie 5.3 
alien_color = "zielony" 
if alien_color == "zielony":
    print("Gratulację, zdobyłeś 5 pkt")

if alien_color == "czerwony":
    print("Gratulację, zdobyłeś 5 pkt")

#zadanie 5.4 
alien_color = "czerwony"
if alien_color =="zielony":
    print("Zobyłeś 5 pkt.")
else: 
    print("Zdobyłes 10 pkt")

alien_color = "czerwony"
if alien_color =="zielony":
    print("Zobyłeś 5 pkt.")
if alien_color != "zielony":
    print("Zdobyłes 10 pkt")

#zadanie 5.5 
alien_color="żółty"
if alien_color == "zielony":
    print("Zdobyłes 5pkt")
elif alien_color =="żółty":
    print("Zdobyłes 10 pkt.")
elif alien_color == "czerwony":
    print("Zdobyłes 15 pkt.")

#zadanie 5.6 
age = 2
if age <= 2:
    print("Jesteś niemowlęciem")
if age >2 and age <4:
    print("Jesteś dzieckiem, które uczy się chodzić")
if age > 4 and age<13:
    print("Jesteś dzieckiem")
if age > 13 and age < 20:
    print("Jesteś nastolatkiem")
if age > 20 and age <65:
    print("Jesteś dorosłym")
else:
    print("Jesteś seniorem")


#zadanie 5.7
favourite_fruits =("kiwi", "pomarańcza", "wiśnia")
if "kiwi" in favourite_fruits:
    print("Naprawdę lubisz kiwi")
if "wiśnia" in favourite_fruits:
    print("Naprawdę lubisz wisnie")
if "brzoskwinie" in favourite_fruits:
    print("Naprawdę lubisz brzoskwinie")
if "pomarańcza" in favourite_fruits:
    print("Naprawdę lubisz pomarańcze")
if "truskawak" in favourite_fruits:
    print("Naprawdę lubisz truskawkig")