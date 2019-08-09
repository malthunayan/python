class Employee:
	def __init__(self,name,age,salary,employment_date,**kwargs):
		self.name=name
		self.age=age
		self.salary=salary
		self.employment_date=employment_date

		for attributes,values in kwargs.items():
			setattr(self,attributes,values)

	def get_working_years(self):
		from datetime import date
		return date.today().year-self.employment_date

	def __str__(self):
		return 'Name: '+self.name+', Age: '+self.age+', Salary: '+self.salary+', Working Years: '

class Manager:
	def __init__(self,name,age,salary,employment_date,bonus_percentage,**kwargs):
		self.name=name
		self.age=age
		self.salary=salary
		self.employment_date=employment_date
		self.bonus_percentage=bonus_percentage

		for attributes,values in kwargs.items():
			setattr(self,attributes,values)

	def get_working_years(self):
		from datetime import date
		return date.today().year-self.employment_date

	def get_bonus(self):
		return self.bonus_percentage*self.salary

	def __str__(self):
		return 'Name: '+self.name+', Age: '+self.age+', Salary: '+self.salary+', Working Years: '


print('Welcome to HR Pro 2019')
employees=[]
managers=[]
dashes='-'*40

while True:
	print('Choose an action to do:')
	print('1. Show employees\n2. Show managers\n3. Add an employee\n4. Add a manager\n5. Exit')
	option=int(input('What would you like to do? '))
	print(dashes)
	if option==1:
		print(employees.__str__())
		print(dashes)
	elif option==2:
		print(managers)
		print(dashes)
	elif option==3:
		employees.append(Employee(input('Name: '),input('Age: '),float(input('Salary: ')),int(input('Employment date: '))))
		print('Employee added successfully!')
	elif option==4:
		managers.append(Manager(input('Name: '),input('Age: '),float(input('Salary: ')),int('Employment date: ')),float(input('Bonus Percentage: ')))
		print('Manager added successfully!')
	elif option==5:
		break
	else:
		print('Error: Please choose a value from 1 to 5.')












