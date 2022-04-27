from flask import Flask, render_template, request
import requests
from addressbook import Contact, AddressBook

app = Flask(__name__)
   
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

addressBook = AddressBook()

def createContacts(numOfUsers, nation):
    contacts = getData(numOfUsers, nation)
    for contact in contacts["results"]:
        first_name = contact["name"]["first"]
        last_name = contact["name"]["last"]
        email = contact["email"]
        phone = contact["phone"]
        photo = contact["picture"]["large"]
        newContact = Contact(first_name, last_name, email, phone, photo)
        addressBook.addAddress(newContact)
    
createContacts(25, 'us')
allAddresses = addressBook.getAllAddresses()

@app.route("/")
def getEntries():
    return render_template('index.html', addresses = allAddresses)

@app.route("/search", methods = ['POST'])
def search():
    search = request.form.get("search")
    return render_template('index.html', addresses = addressBook.findAllMatching(search))

if __name__ == "__main__":
    app.run()