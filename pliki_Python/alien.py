alien_0 = {"color":"zielony", "points":5}
print(alien_0["color"])
print(alien_0["points"])

new_points=alien_0["points"]
print(f"Zdobyłeś {new_points} punktów.")

alien_0["x_postion:"]=0
alien_0["y_position"]=25
print(alien_0)

alien_0= {}
alien_0["color"] = "zielony"
alien_0["points"] = 5
print(alien_0)

alien_0 ={"color":"zielony"}
print(f'Obcy ma kolor {alien_0["color"]}')
alien_0["color"] = "żółty"
print(f"Obcy ma teraz kolor {alien_0['color']}.")

alien_0 = {"x_position":0, "y_postion":25, "speed":"szybko"}
print(f"Początkowa wartość x-position: {alien_0['x_position']}")
#ustalenie z o ile obcy powinien się przesunąć 
if alien_0["speed"]=="wolno":
    x_increment = 1
elif alien_0["speed"] =="średnio":
    x_increment = 2
else:
    #obcy musi zapierdalać 
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"Nowa wartość x-position: {alien_0['x_position']}")

alien_0 ={"color":"zielony", "points":5}
print(alien_0)

del alien_0['points']
print(alien_0)