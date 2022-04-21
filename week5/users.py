import requests

class User:
    def __init__(self, first_name, last_name, email, username, password, uuid, phone, cell, pic_large, pic_thumb):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.uuid = uuid
        self.phone = phone
        self.cell = cell
        self.pic_large = pic_large
        self.pic_thumb = pic_thumb
    def getFirstName(self):
        return self.first_name
    def setFirstName(self, first_name):
        self.first_name = first_name
    def getLastName(self):
        return self.last_name
    def setLastName(self, last_name):
        self.last_name = last_name
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email
    def getUsername(self):
        return self.username
    def setUsername(self, username):
        self.username = username
    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password
    def getUuid(self):
        return self.uuid
    def setUuid(self, uuid):
        self.uuid = uuid
    def getPhone(self):
        return self.phone
    def setPhone(self, phone):
        self.phone = phone
    def getCell(self):
        return self.cell
    def setCell(self, cell):
        self.cell = cell
    def getPicLarge(self):
        return self.pic_large
    def setPicLarge(self, pic_large):
        self.pic_large = pic_large
    def getPicThumb(self):
        return self.pic_thumb
    def setPicThumb(self, pic_thumb):
        self.pic_thumb = pic_thumb
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'

class AuthorizedUsers():
    def __init__(self):
        self.authUsers = []
    def addUser(self, user):
        self.authUsers.append(user)
    def showUsers(self):
        for user in self.authUsers:
            print(user)

def getData(numUsers, nation):
    try:
        response = requests.get(f'https://randomuser.me/api/?results={numUsers}&nat={nation}', timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON
    except requests.exceptions.HTTPError as errh:
        print(f"HTTPError - {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error - {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout - {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception - {err}")

authorizedUsers = AuthorizedUsers()

def createUsers(numOfUsers, nation):
    users = getData(numOfUsers, nation)
    for user in users["results"]:
        first_name = user["name"]["first"]
        last_name = user["name"]["last"]
        email = user["email"]
        username = user["login"]["username"]
        password = user["login"]["password"]
        uuid = user["login"]["uuid"]
        phone = user["phone"]
        cell = user["cell"]
        pic_large = user["picture"]["large"]
        pic_thumb = user["picture"]["thumbnail"]
        newUser = User(first_name, last_name, email, username, password, uuid, phone, cell, pic_large, pic_thumb)
        authorizedUsers.addUser(newUser)
    
createUsers(10, 'us')
authorizedUsers.showUsers()