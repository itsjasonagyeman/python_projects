import json

contacts = {
    'Jason' : {'phone': '0244499315', 'email':'agyemanjasonnhyira@gmail.com'},
    'Abby' : {'phone': '0244498215', 'email':'abbyjasonnhyira@gmail.com'},
    'Pierre' : {'phone': '0244497214', 'email':'pierrejasonnhyira@gmail.com'},
}

class Contact:
    def view(self):
        for name, info in contacts.items():
            print(f'{name}: {info}')

    def add(self):
        name = input('Name? ')
        phone = input('Number?')
        email = input('Email?')

        contacts[name] = {'phone': phone, 'email': email}
        Contact().view()

    def search(self):
        search = input('Search? ')
        if search in contacts:
            print(contacts[search])
        else:
            print('Contact not found')

    def update(self):
        update = input('Who do you want to update? ')
        print(contacts[update])
        ask = input('Update? 1. Phone, 2. email ')
        if ask == '1':
            newphone = input('New phone number? ')
            contacts[update]['phone'] = newphone
            print(contacts[update])
        elif ask == '2':
            newemail = input('New phone email? ')
            contacts[update]['email'] = newemail
            print(contacts[update])

    def delete(self):
        delete = input('Who do you want to delete? ')
        if delete in contacts:
            del contacts[delete]
            print(contacts)



while True:
    a = Contact()
    b = input('What do you want to do? ')
    if b.lower() == 'view':
        a.view()
    elif b.lower() == 'add':
        a.add()
    elif b.lower() == 'search':
        a.search()
    elif b.lower() == 'update':
        a.update()
    elif b.lower() == 'delete':
        a.delete()
    elif b.lower() == 'end':
        with open('contacts.txt', 'w') as file:
            json.dump(contacts, file)
        break
