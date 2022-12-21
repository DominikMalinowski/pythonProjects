from user import User

class Privileges():
    def __init__(self):
        """Inicjalizacja klasy"""
        
    def show_privileges(self):
        privileges = ['może dodać post','może usunąć post','może zbanować użytkownika']
        print("Admin może wykonać nast. akcje:")
        for privilege in privileges:
            print(f'\t- {privilege}')

class Admin(User):

    privileges = Privileges()

    def __init__(self, first_name, last_name, age, sex):
        """Inicjalizacja klasy podrzędnej - Admin"""
        super().__init__(first_name,last_name, age, sex)
        """Inicjalizacja klasy nadrzędnej (superklasy) - User"""


another_admin = Admin('zenon,','kowalczyk',29,'m')
another_admin.privileges.show_privileges()