#zadanie 7.4 
dodatek = input("Proszę podać wybrany dodatek do pizzy") 
dodatek += ("Jeśli to wszystkie dodatki proszę wpisać 'koniec'")

whlie True:
    if dodatek != "koniec":
        print(f"{dodatek} został dodany do pizzy") 
    else: 
        break 