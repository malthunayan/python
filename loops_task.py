item=[]
price=[]
quantity=[]

while True:
	item.append(input('Item (enter "done" when finished): '))
	if item[-1].lower()=='done':
		break
	price.append(float(input('Price: ')))
	quantity.append(int(input('Quantity: ')))
del item[-1]

receipt={'item name':item,'price':price,'quantity':quantity}

print('-'*len('receipt')*2+'\n    Receipt\n'+'-'*len('receipt')*2)

x=0
total_price=[]
while x<len(price):
	total_price.append(price[x]*quantity[x])
	print('%d %s '%(quantity[x],item[x])+str(price[x])+'KD')
	x+=1
print('-'*len('receipt')*2)


print('Total: '+str(sum(total_price))+'KD')