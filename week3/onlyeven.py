def prompt():
    pos_num = input("Enter a positive number: ")
    return pos_num

def countDown(num):
    for num in range(0, int(num)+1, 2):
        print(num)

pos_num = prompt()

while(not pos_num.isdigit()):
    pos_num = prompt()
    
countDown(pos_num)