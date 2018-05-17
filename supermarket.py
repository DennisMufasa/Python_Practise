invoices=[]
item=""
quant=0
price=0
grandTotal=0

while True:
    item = input("Enter the item bought")

    if item=="stop":
        break

    quant = input("How many items do you require?")
    price = input("How much does the item cost?")

    invoices.append({"items":item,"quant":quant,"price":price})

for invoice in invoices:

    item=invoice["items"]
    quant=int(invoice["quant"])
    price=int(invoice["price"])

    total=quant*price
    grandTotal+=total

    print("Item-",item,"quantity-",quant,"Cost per Item-",price,'\n',"Total item Cost-",total)
print("Grand Total: ",grandTotal)