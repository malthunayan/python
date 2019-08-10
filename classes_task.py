from datetime import date

class Employee:
	def __init__(self,name,age,salary,employment_date,**kwargs):
		self.name=name
		self.age=age
		self.salary=salary
		self.employment_date=employment_date

		for attributes,values in kwargs.items():
			setattr(self,attributes,values)

	def get_working_years(self):
		return date.today().year-self.employment_date

class Manager(Employee):
	def __init__(self,name,age,salary,employment_date,bonus_percentage,**kwargs):
		super().__init__(name, age, salary, employment_date)
		self.bonus_percentage=bonus_percentage

		for attributes,values in kwargs.items():
			setattr(self,attributes,values)

	def get_working_years(self):
		return date.today().year-self.employment_date

	def get_bonus(self):
		return self.bonus_percentage*self.salary

print('Welcome to HR Pro 2019')
dashes='-'*50
employee_list=[]
manager_list=[]

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
			if len(employee_list)==0:
				print('No employees have been added to the list yet.')
			for employee in employee_list:
				print('Name: '+employee.name+', Age: '+str(employee.age)+', Salary: '+str(employee.salary)+', Working Years: '+str(employee.get_working_years()))
			print(dashes)
		elif option==2:
			if len(manager_list)==0:
				print('No managers have been added to the list yet.')
			for manager in manager_list:
				print('Name: '+manager.name+', Age: '+str(manager.age)+', Salary: '+str(manager.salary)+', Working Years: '+str(manager.get_working_years())+', Bonus: '+str(manager.get_bonus()))
			print(dashes)
		elif option==3:
			employee=Employee(input('Name: ').title(),input('Age: '),float(input('Salary: ')),int(input('Employment date: ')))
			employee_list.append(employee)
			print('\nEmployee added successfully!\n')
		elif option==4:
			manager=Manager(input('Name: ').title(),input('Age: '),float(input('Salary: ')),int(input('Employment date: ')),float(input('Bonus Percentage: ')))
			manager_list.append(manager)
			print('\nManager added successfully!\n')
		elif option==5:
			break
		else:
			print('Error: Please choose a value from 1 to 5.')
			print(dashes)