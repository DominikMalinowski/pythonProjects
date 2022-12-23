import pizza 

pizza.make_pizza(40, 'peperoni')
pizza.make_pizza(30, 'pieczarki','zielona papryka','podwójny ser')

from pizza import make_pizza 
make_pizza(50, 'salami')
make_pizza(75, 'sól', 'pieprz')

from pizza import make_pizza as mp 
mp(25, 'ziemniaki')

import pizza as p 
p.make_pizza(12,'suchy chleb dla konia')