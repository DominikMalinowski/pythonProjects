def spam():
    eggs = 'Zmienna lokalna funkcji spam().'
    print(eggs)

def bacon():
    eggs = 'Zmienna lokalna funkcji bacon().'
    print(eggs)
    spam()
    print(eggs)

eggs = 'Zmienna globalna'
bacon()
print(eggs)
