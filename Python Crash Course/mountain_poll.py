responses ={} 

#tworzenie flagi wskazującej czy ankieta jest aktywna 
polling_active = True

while polling_active: 
    name = input("\n Jak masz na imię ?")
    response = input("\n Na jaki szczyt chciałbyś się wspiąć ?")

#umieszczenie odpowiedzi w słowniku 
responses[name] = response 

#ustalenie czy ktokolwiek chce jeszcze wziąc udział w ankiecie 
repeat = input("Czy ktokolwiek chce jeszcze wziąc udział w ankiecie ? (tak/nie)")
if repeat == "nie":
        polling_active=False 

#ankieta została zakończona i wyświetlone zostaną jej wyniki 
print("\n--- Wyniki ankiety---")
for name, response in responses.items():
    print(f"{name} chciałby wspiąć sięna {response}")



