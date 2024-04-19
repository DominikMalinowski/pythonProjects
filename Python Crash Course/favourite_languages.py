favorite_languages = {
    "janek":"python",
    "sara":"c",
    "edward": "ruby",
    "paweł": "python",}

language_sara = favorite_languages['sara'].title()
print(f"Ulubiony język Sary to {language_sara}\n")

for name,language in favorite_languages.items():
    print(f"Ulubiony język użytkownika {name.title()} to język {language.title()}")

for name in favorite_languages.keys():
    print(name.title())

friends=["paweł", "sara"]
for name in favorite_languages:
    if name in friends:
        language = favorite_languages[name].title()
        print(f"Witaj, {name.title()}! Widzę, ze twój ulubiony język programowania jest {language}")
    else: 
        print(f"Witaj, {name.title()}")

favorite_languages = {
    'janek':'python',
    'sara':'c',
    'edward': 'ruby',
    'paweł': 'python',
    }

if 'elżbieta' not in favorite_languages.keys():
    print("Elżbieto, weź udział w naszej ankiecie")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, dziękuję za udział w ankiecie.")

print(f"\n W ankieice zostały wymienione nast. języki programowania:")
for language in favorite_languages.values():
    print(f"\t{language.title()}")

print("W ankiecie zostały wymienione nastepujące języki programowania:")
for language in set(favorite_languages.values()):
    print(language.title())

favorite_languages = {
    'zenek':[],
    'janek':['python','ruby'],
    'sara':['c'],
    'edward': ['ruby', 'go'],
    'paweł': ['python','haskell'],
    }
for name,languages in favorite_languages.items():
    if len(languages)>1:
        print(f"\n Ulubione języki programowania użytkownika {name.title()} to:")
        for language in languages:
            print(f"\t {language.title()}")
    else:
        print(f"\n Ulubiony język programowania użytkownika {name.title()} to {language.title()}")

