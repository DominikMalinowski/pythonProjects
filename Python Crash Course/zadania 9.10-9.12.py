#zadanie 9.10 
from restaurant import Restaurant 

nowa_knajpa = Restaurant('pod_psem','wietnamskiej')
nowa_knajpa.describe_restaurant()

#zadanie 9.11
#from user_admin_privileges import User, Admin, Privileges

#nowy_admin = Admin('jan','qn',88,'m')
#nowy_admin.privileges.show_privileges()

#zadanie 9.12 
from new_user import User 
from new_admin_privileges import Privileges, Admin

another_admin = Admin('zenon,','kowalczyk',29,'m')
another_admin.privileges.show_privileges()
