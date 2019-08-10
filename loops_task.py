items=[]
while True:
	name=input('Item (enter "done" when finished): ')
	if name.lower()=='done':
		break
	price=float(input('Price: '))
	quantity=int(input('Quantity: '))
	items.append({'name':name,'price':price,'quantity':quantity})

print('-'*len('receipt')*2+'\n   Receipt\n'+'-'*len('receipt')*2)

total_price=0
for item in items:
	total_price+=item['price']*item['quantity']
	print('%d %s %.3fKD'%(item['quantity'],item['name'],item['price']))

print('-'*len('receipt')*2)
print('Total: %.3fKD'%(total_price))