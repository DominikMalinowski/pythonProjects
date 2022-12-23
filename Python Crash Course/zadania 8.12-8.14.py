#zadanie 8.12
def kanapka(*skladniki): 
    print(f"\nTwoja zamówiona kanapka składać się bedzie z:")
    for skladnik in skladniki:
        print(f"- {skladnik}")

kanapka('ser','szynka','ogórek')
kanapka("góóóóóówno")
kanapka("chleb", "bułka tarta")

#zadanie 8.13 
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info 

user_profile = build_profile('albert', 'einstein', location='princeton', field ='fizyka')
print(user_profile)

user_profile = build_profile('Dominik', 'Malinowski', wzrost='1,89m', plec="mężczyzna", dupa='zajebista')
print(user_profile)

#zadanie 8.14
def samochod(marka, model, **info):
    info['marka_samochodu'] = marka
    info['model_samochodu'] = model
    return info

brumbrum = samochod('Reanult', 'Megane', kolor='srebrno-niebieski', silnik='1.6')
print(brumbrum)