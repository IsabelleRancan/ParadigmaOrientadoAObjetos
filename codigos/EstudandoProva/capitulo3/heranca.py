class Contact:
    all_contacts = []
 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        return (Contact.all_contacts)

teste = Contact('isabelle', 'isa')
print(teste)