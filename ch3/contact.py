class ContactList(list):
    """Extending built-ins
    One interesting use of this kind of inheritance is adding functionality to built-in classe """
    def search(self,name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts= ContactList()

    """def __init__(self, **kwargs):
        for arg in kwargs.items():
            print(arg)"""

    def __init__(self,name,email):
       self.name = name
       self.email = email
       self.all_contacts.append(self) #Contact.all_contacts.append(self)

class SubContact(Contact):
    """basic inheritance"""
    def order(self):
        print("this is sub class object")

class Friend(Contact):
    """Overriding and super"""
    """def __init__(self,name,email,phone):
        super().__init__(name,email)
        self.phone = phone """

    " Different sets of arguments "
    def __init__(self,phone,**kwargs): #def __init__(self,name,email,phone):
        super().__init__(**kwargs) #super().__init__(name,email)
        self.phone = phone


    def __str__(self):
        print("Friend phone {0} name {1} email {2}".format(self.phone,self.name,self.email))




if __name__ == "__main__":
    c = Contact("Alaa","alaa@gmail.com")
    s= SubContact("Arwa","arwa@gmail.com")
    s2=SubContact("Ahmed Ali","ahmed@gmail.com")
    s3= SubContact("Ahmed Tamer", "ahmed123@gmail.com")

    print(c.all_contacts)
    print("--------------")
    print(s.all_contacts)
    s.order()
    # c.order() AttributeError: 'Contact' object has no attribute 'order'
    matching_contact = Contact.all_contacts.search("Ahmed")
    print(matching_contact)
    print([c.name for c in Contact.all_contacts.search("Ahmed")])

    #friend = Friend("Arwa","arwa@gmail.com","0244778741")
    " Different sets of arguments "
    friend = Friend("0244778741",name="Arwa",email="arwa@gmail.com")
    friend.__str__() #Friend phone 0244778741 name Arwa email arwa@gmail.com


