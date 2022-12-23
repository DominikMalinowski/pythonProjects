while True:
    print('Kim jestes ?')
    name = input()
    if name != 'Janek':
        continue
    print('Witaj Janek, jakie jest haslo ?')
    password = input()
    if password =='miecznik':
        break
    print('Masz dostep')
