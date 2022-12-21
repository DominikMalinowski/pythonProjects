#zadanie 3.4 
goscie=["KAROL","Bartek","Monika"]
print(f'Witaj na obiedzie {goscie[1].upper()}')
print(f'Zapraszam i smacznego {goscie[2].lower()}')
print(f'Siadaj, nałoże Ci zmieniaczków {goscie[0].title()}u')

#zadanie 3.5 
print(f'Niestety {goscie[2].title()} nie może przyjść')

del goscie[2]
goscie.append('monika')
print (goscie)
goscie_bez_moniki = goscie.pop(2)
print (goscie_bez_moniki)
goscie.append('Oskar')
print(f'Witaj na obiedzie {goscie[1].upper()}')
print(f'Zapraszam i smacznego {goscie[2].lower()}')
print(f'Siadaj, nałoże Ci zmieniaczków {goscie[0].title()}u')

#zadanie 3.6 
goscie.insert(0, "Kitku")
goscie.insert(2, "Ola")
goscie.append("Mateusz")
print(f'Zapraszam Cię na jutrzejszy obiad {goscie[0].title()}')
print(f'Zapraszam Cię na jutrzejszy obiad {goscie[1].title()}')
print(f'Zapraszam Cię na jutrzejszy obiad {goscie[2].title()}')
print(f'Zapraszam Cię na jutrzejszy obiad {goscie[3].title()}')
print(f'Zapraszam Cię na jutrzejszy obiad {goscie[4].title()}')
print(f'Zapraszam Cię na jutrzejszy obiad {goscie[5].title()}')
print('Niestety, na obiad mogę zaprosic tyko dwie osoby')

goscie_usunieci = goscie.pop(2)
print(f'Niestety, nastapiła zmiana planów {goscie_usunieci.title()}')
goscie_usunieci = goscie.pop(2)
print(f'Niestety, nastapiła zmiana planów {goscie_usunieci.title()}')
goscie_usunieci = goscie.pop(2)
print(f'Niestety, nastapiła zmiana planów {goscie_usunieci.title()}')
goscie_usunieci = goscie.pop(2)
print(f'Niestety, nastapiła zmiana planów {goscie_usunieci.title()}')
print(f'Mrau, zapraszam Cię na obiad {goscie[0].title()}')
print(f'Zapraszam Cię na kebsa {goscie[1].title()}')
del goscie [0]
del goscie [0]
print(goscie)

len(goscie)