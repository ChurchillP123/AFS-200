p_des = input("Please enter the product description: ")
p_quan = int(float(input(f"How many of item {p_des} are being purchased? ")))
reg_price = float(input("What is the regular price? "))
TAX = 0.065

print("Your Receipt\n------------")

if reg_price > 39.99:
    dis_price = reg_price * 0.75
elif reg_price > 19.99:
    dis_price = reg_price * 0.85
else:
    dis_price = reg_price
    
sales_tax = p_quan * dis_price * TAX
total = p_quan * dis_price + sales_tax
dis_total = (p_quan * reg_price) - total

print(f"{p_quan} {p_des} @ ${dis_price:,.2f} each")
print(f"Sales Tax ${sales_tax:,.2f}")
print(f"Total amount due ${total:,.2f}")
print(f"You saved ${(dis_total):,.2f} today.")