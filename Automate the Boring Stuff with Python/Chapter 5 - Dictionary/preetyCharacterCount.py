import pprint
message = 'Był jasny, zimny  dzien kwietniowy i zegary biły trzynastą'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

pprint.pprint(count)
print(count)
