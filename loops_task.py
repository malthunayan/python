items=[]
while True:
	name=input('Item (enter "done" when finished): ')
	if name.lower()=='done':
		break
	price=float(input('Price: '))
	quantity=int(input('Quantity: '))
	items.append({'name':name,'price':price,'quantity':quantity})

print('-'*len('receipt')*2+'\n   Receipt\n'+'-'*len('receipt')*2)

total_price=[]
for x in range(len(items)):
	total_price.append(items[x]['price']*items[x]['quantity'])
	print('%d %s %.3fKD'%(items[x]['quantity'],items[x]['name'],items[x]['price']))

print('-'*len('receipt')*2)
print('Total: %.3fKD'%(sum(total_price)))