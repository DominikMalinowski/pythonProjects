#! python 3
# pw py niebezpieczny program menadżera haseł
PASSWORD = {'email':'F7fke93#($<of',
            'blog':'llkjnoiweih*&)(FLSAKJ#',
            'luggage':'12345'}

import sys
if len(sys.argv)<2:
    print('Użycie: Python pw.py [konto] - skopiowanie hasła wskazanego konta')
    sys.exit()

account = sys.argv[1]
