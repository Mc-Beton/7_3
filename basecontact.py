class BaseContact:
    def __init__(self, name, last_name, number, e_mail):
        self.name = name
        self.last_name = last_name
        self.number = number
        self.e_mail = e_mail

    def __str__(self):
        return f"{self.name} {self.last_name} {self.e_mail}"


    def contact(self):
        return f"Dailing +48 {self.number} and calling to {self.name} {self.last_name}"
 
    @property
    def label_length(self):
        imie = len(self.name)
        nazwisko = len(self.last_name)
        return f"{imie} {nazwisko}"