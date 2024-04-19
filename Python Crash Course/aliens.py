alien_0 = {"color":"zielony","points":5}
alien_1 = {"color":"żółty", "points": 10}
alien_2 = {"color":"czerwony","points": 15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#utworzenie pustej listy "aliens"
aliens = []
#utworzenie 30 zielonych obcych 
for alien_number in range(30):
    new_alien = {"color":"zielony", "points":5, "speed":"wolno"}
    aliens.append(new_alien)
#wyświetlenie pierwszych 5 obcych 
for alien in aliens[:5]:
    print(alien)
print("...")

#wyświetlenie całkowitej liczny obiektów 
print(f"Całkowita liczba utworzonych ziellonych obcych to: {len(aliens)}")

#utworzenie pustej listy "aliens"
aliens = []
#utworzenie 30 zielonych obcych 
for alien_number in range(30):
    new_alien = {"color":"zielony", "points":5, "speed":"wolno"}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien["color"]== "zielony":
        alien["color"] = "żółty"
        alien["points"] = 10
        alien["speed"] = "średnio"

for alien in aliens[:5]:
    print(alien)
print("...")