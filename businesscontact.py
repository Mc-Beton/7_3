from basecontact import BaseContact

class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        return f"Dailing +48 {self.business_phone} and calling to {self.name} {self.last_name}"