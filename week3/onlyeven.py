def prompt(isValid = True):
    if(isValid):
        return input("Enter a positive number: ")
    return input("Invalid Entry. Please enter a positive number: ")
    
def countDown(num):
    for num in range(0, int(num)+1, 2):
        print(num)

pos_num = prompt()

while(not pos_num.isdigit()):
    pos_num = prompt(False)
    
countDown(pos_num)