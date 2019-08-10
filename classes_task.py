class Employee:
	employees=[]
	def __init__(self,name,age,salary,employment_date,**kwargs):
		self.name=name
		self.age=age
		self.salary=salary
		self.employment_date=employment_date
		Employee.employees.append(self.name)
		Employee.employees.append(self.age)
		Employee.employees.append(self.salary)
		Employee.employees.append(self.get_working_years())

		for attributes,values in kwargs.items():
			setattr(self,attributes,values)

	def get_working_years(self):
		from datetime import date
		return date.today().year-self.employment_date

	# def __str__(self):
	# 	x=0
	# 	while x<len(Employee.employees):
	# 		return 'Name: '+str(Employee.employees[x])+', Age: '+str(Employee.employees[x+1])+', Salary: '+str(Employee.employees[x+2])+', Working Years: '+str(Employee.employees[x+3])
	# 		x+=4

class Manager:
	managers=[]
	def __init__(self,name,age,salary,employment_date,bonus_percentage,**kwargs):
		self.name=name
		self.age=age
		self.salary=salary
		self.employment_date=employment_date
		self.bonus_percentage=bonus_percentage
		Manager.managers.append(self.name)
		Manager.managers.append(self.age)
		Manager.managers.append(self.salary)
		Manager.managers.append(self.get_working_years())
		Manager.managers.append(self.get_bonus())

		for attributes,values in kwargs.items():
			setattr(self,attributes,values)

	def get_working_years(self):
		from datetime import date
		return date.today().year-self.employment_date

	def get_bonus(self):
		return self.bonus_percentage*self.salary

	# def __str__(self):
	# 	return 'Name: '+self.name+', Age: '+str(self.age)+', Salary: '+str(self.salary)+', Working Years: '+str(self.get_working_years())+', Bonus: '+str(self.get_bonus())


print('Welcome to HR Pro 2019')
dashes='-'*50

while True:
	print('Choose an action to do:')
	print('1. Show employees\n2. Show managers\n3. Add an employee\n4. Add a manager\n5. Exit')
	try:
		option=int(input('What would you like to do? '))
	except ValueError:
		print(dashes)
		print('Error: Please choose a value from 1 to 5.')
		print(dashes)
	else:
		print(dashes)
		if option==1:
			if len(Employee.employees)==0:
				print('No employees have been added to the list yet.')
			x=0
			while x<len(Employee.employees):
				print('Name: '+Employee.employees[x]+', Age: '+str(Employee.employees[x+1])+', Salary: '+str(Employee.employees[x+2])+', Working Years: '+str(Employee.employees[x+3]))
				x+=4
			print(dashes)
		elif option==2:
			if len(Manager.managers)==0:
				print('No managers have been added to the list yet.')
			x=0
			while x<len(Manager.managers):
				print('Name: '+Manager.managers[x]+', Age: '+str(Manager.managers[x+1])+', Salary: '+str(Manager.managers[x+2])+', Working Years: '+str(Manager.managers[x+3])+', Bonus: '+str(Manager.managers[x+4]))
				x+=5
			print(dashes)
		elif option==3:
			emp=Employee(input('Name: ').title(),input('Age: '),float(input('Salary: ')),int(input('Employment date: ')))
			print('\nEmployee added successfully!\n')
		elif option==4:
			man=Manager(input('Name: ').title(),input('Age: '),float(input('Salary: ')),int(input('Employment date: ')),float(input('Bonus Percentage: ')))
			print('\nManager added successfully!\n')
		elif option==5:
			break
		else:
			print('Error: Please choose a value from 1 to 5.')
			print(dashes)