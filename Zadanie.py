from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, last_name, number, e_mail):
        self.name = name
        self.last_name = last_name
        self.number = number
        self.e_mail = e_mail

    def __str__(self):
        return f"{self.name} {self.last_name} {self.e_mail}"


    def contact(self):
        return f"Wybieram numer +48 {self.number} i dzwonię do {self.name} {self.last_name}"
 
    @property
    def label_length(self):
        imie = len(self.name)
        nazwisko = len(self.last_name)
        return f"{imie} {nazwisko}"

class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone
    

base_cards = []
business_cards = []

def create_contacts(typ, amount):
    
    for m in range(amount):
        i = fake.name()
        j = fake.safe_email()
        k = i.split()
        m = fake.phone_number()
        if typ == BaseContact:
            base_cards.append(BaseContact(name = k[0], last_name=k[1], number = m, e_mail = j))
        elif typ == BusinessContact:
            n = fake.job()
            p = fake.company()
            r = fake.phone_number()
            business_cards.append(BusinessContact(name = k[0], last_name=k[1], number = m, e_mail = j, job = n, company = p, business_phone = r))
              


create_contacts(BaseContact, 3)
create_contacts(BusinessContact, 3)

for i in base_cards:
    print(i)

for i in business_cards:
    print(i)

print(base_cards[1].contact())
print(base_cards[1].label_length)

print(business_cards[1].contact())
print(business_cards[1].label_length)
