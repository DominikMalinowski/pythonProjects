def greet_user(names): 
    """Wyświetla proste powitanie każdemu użytkownikowi z listy"""
    for name in names: 
        msg = f"Witaj, {name.title()}"
        print(msg)

username = ['halina', 'grazyna', 'marzena']
greet_user(username)