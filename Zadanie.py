from faker import Faker
fake = Faker()
import time

# Define main class
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

# Define new sub-class
class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone
    
# Define lists of cards
base_cards = []
business_cards = []

# Function to calculate time to execute a chosen function
def how_long(func):
    def wrap(*args):
        start = time.time()
        ret = func(*args)
        end = time.time()
        print(end - start)
        
    return wrap

# Function to generate random personal data
@how_long
def create_contacts(typ, amount):
    
    for m in range(amount):
        i = fake.first_name()
        j = fake.safe_email()
        k = fake.last_name()
        m = fake.phone_number()
        if typ == BaseContact:
            base_cards.append(BaseContact(name = i, last_name=k, number = m, e_mail = j))
        elif typ == BusinessContact:
            n = fake.job()
            p = fake.company()
            r = fake.phone_number()
            business_cards.append(BusinessContact(name = i, last_name=k, number = m, e_mail = j, job = n, company = p, business_phone = r))
    
# Function to print out possible commands
def print_help():
    print("Here we have a list of available commands")
    print("make base cards - generate random cards with personal data")
    print("make business cards - generate random business cards")
    print("show - print out generated base or business cards")
    print("call - from a list of base or business cards call a person by his/her name")
    print("exit - terminate program")

def show(a):
    if a == "base cards":
        for i in base_cards:
            print(i)
        
    elif a == "business cards":
        for i in business_cards:
            print(i)
        


    


def call():
    a = input("From which list of contacts would you like to call? \n base cards \n business cards \n")
    show(a)
    b = input("Type in the persons first name you would like to contact ")
    if a == "base cards":
        for i in base_cards:
            if b == str(i.name):
                print(i.contact())
        
    elif a == "business cards":
        for i in business_cards:
            if b == str(i.name):
                print(i.contact())

def length():
    a = input("From which list of contacts would you like to check the length of names? \n base cards \n business cards \n")
    show(a)
    b = input("Type in the persons first name you would like to check ")
    if a == "base cards":
        for i in base_cards:
            if b == str(i.name):
                print(i.label_length)
        
    elif a == "business cards":
        for i in business_cards:
            if b == str(i.name):
                print(i.label_length)
    





# Available commands
def task():
    while True:
        task1 = input("What would you like to do? ")
        if task1 == "help_me":
            print_help()
        
        elif task1 == "make base cards":
            a = int(input("How many random base cards would you like to create? "))
            create_contacts(BaseContact, a)
        
        elif task1 == "make business cards":
            a = int(input("How many random business cards would you like to create? "))
            create_contacts(BusinessContact, a)
        
        elif task1 == "show":
            a = input("Which cards would you like to see? \n base cards \n business cards \n")
            show(a)
        
        elif task1 == "call":
            call()
        
        elif task1 == "length":
            length()
        
        elif task1 == "exit":
            print("bye")
            break
        else:
            print("there is no such command, type help_me for list of available commands")
        
# Call out the program
if __name__ == "__main__":
    print("Hello! I am a simple program to do some stuff. Wanna check me out? Type in help_me for commands ;)")
    task()

