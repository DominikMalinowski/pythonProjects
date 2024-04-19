#zadanie 8.9 
#komunikaty = ['dupa','kupa','z trupa']
#def show_messages(message):
#    for mes in message:
#        print(mes)

#show_messages(komunikaty)

#zadanie 8.10 
komunikaty = ['dupa','kupa','z trupa']
#def show_messages(message):
#    for mes in message:
#        print(mes)

#show_messages(komunikaty)

sent_message=[]
def send_message(wiadomosci):
    print(f"Tu jest poczatkowa lista: {wiadomosci}")
    for wiadomosc in wiadomosci:
        print(wiadomosc)
        sent_message.append(wiadomosc)

send_message(komunikaty)

print(f"Tu jest ostateczna lista: {sent_message}")

#zadanie 8.11
komunikaty = ['dupa','kupa','z trupa']
def show_messages(message):
    for mes in message:
        print(mes)

show_messages(komunikaty)

sent_message=[]
def send_message(wiadomosci):
    print(f"Tu jest poczatkowa lista: {wiadomosci}")
    for wiadomosc in wiadomosci:
        print(wiadomosc)
        sent_message.append(wiadomosc)

send_message(komunikaty)

print(f"Tu jest ostateczna lista: {sent_message}")