item=[]
price=[]
quantity=[]
x=0
while not "done" in item:
	item.append(input('Item (enter "done" when finished): '))
	if item[x].lower()!='done':
		price.append(float(input('Price: ')))
		quantity.append(int(input('Quantity: ')))
		x=x+1
item.pop()

receipt={}
receipt['item name']=item
receipt['price']=price
receipt['quantity']=quantity
print(receipt)