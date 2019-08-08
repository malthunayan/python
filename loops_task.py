item=[]
while True:
	name=input('Item (enter "done" when finished): ')
	if name.lower()=='done':
		break
	price=float(input('Price: '))
	quantity=int(input('Quantity: '))
	item.append({'name':name,'price':price,'quantity':quantity})

print(item)
print('-'*len('receipt')*2+'\n    Receipt\n'+'-'*len('receipt')*2)

x=0
total_price=[]
for x in range(len(item)):
	total_price.append(item[x]['price']*item[x]['quantity'])
	print('%d %s %.3fKD'%(item[x]['quantity'],item[x]['name'],item[x]['price']))
	x+=1

print('-'*len('receipt')*2)
print('Total: %.3fKD'%(sum(total_price)))