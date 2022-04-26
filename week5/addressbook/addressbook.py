import requests

class Contact():
    def __init__(self, first_name, last_name, email, phone, photo):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.photo = photo
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone
    def getPhoto(self):
        return self.photo
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    def __rep__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
        return results