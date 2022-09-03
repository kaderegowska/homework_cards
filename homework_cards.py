from faker import Faker
fake = Faker()

class BaseContact:
   def __init__(self, first_name, last_name, phone, email):
       self.first_name = first_name
       self.last_name = last_name
       self.phone = phone
       self.email = email
   def contact(self):
       print(f"Wybieram nr {self.phone} i dzwonię do {self.first_name} {self.last_name}")
   @property
   def label_lenght(self):
       print(len(self.first_name) + len(self.last_name))

class BusinessContact(BaseContact):
   def __init__(self, occupation, company, business_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.occupation = occupation
       self.company = company
       self.business_number = business_number
   def contact(self):
       print(f"Wybieram {self.business_number} i dzwonię do {self.first_name} {self.last_name}")



def create_contact():
    type = input("Rodzaj wizytówki podstawowa/biznesowa: ")
    amount = int(input("Liczba wizytówek: "))
    if type == "podstawowa":
        for i in range(amount):
            print(fake.name(), fake.email(), fake.phone_number())
    elif type == "biznesowa":
        for i in range(amount):
            print(fake.name(), fake.email(), fake.phone_number(), fake.company(), fake.job())

create_contact()

