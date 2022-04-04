p_des = input("Please enter the product description: ")
p_quan = int(float(input(f"How many of item {p_des} are being purchased? ")))
reg_price = float(input("What is the regular price? "))
TAX = 0.065

print("Your Receipt\n------------")

if reg_price > 39.99:
    dis_price = reg_price - (reg_price * 0.25)
    sales_tax = (dis_price * TAX)
    orig_total = p_quan * reg_price + sales_tax
    dis_total = (p_quan * dis_price) + sales_tax
elif reg_price > 19.99:
    dis_price = reg_price - (reg_price * 0.15)
    sales_tax = dis_price * TAX
    orig_total = p_quan * reg_price + sales_tax
    dis_total = (p_quan * dis_price) + sales_tax
else:
    dis_price = reg_price
    sales_tax = dis_price * TAX
    orig_total = p_quan * reg_price + sales_tax
    dis_total = (p_quan * dis_price) + sales_tax

print(f"{p_quan} {p_des} @ ${dis_price} each")
print(f"Sales Tax ${sales_tax:,.2f}")
print(f"Total amount due ${dis_total:,.2f}")
print(f"You saved ${(orig_total - dis_total):,.2f} today.")