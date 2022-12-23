#zadanie 8.15 
#wykonane w modułach print_models i print_functions

#zadnie 8.16
import formatted_name
print(formatted_name.get_formatted_name('adam','małysz'))

from formatted_name import get_formatted_name
print(get_formatted_name('bolesław','prus'))

from formatted_name import get_formatted_name as gfn 
print(gfn('peter','parker'))

import formatted_name as fn 
print(fn.get_formatted_name('john','wick'))

from formatted_name import *
print(formatted_name.get_formatted_name('rambo','bambo'))

#zadanie 8.17 
#sprawdzenie stylu zadań 
