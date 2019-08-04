print("Hello and welcome to the Python Birthday Calculator!\n")

def check_birthdate(d,m,y):
	from datetime import date
	if y>date.today().year:
		return False
	elif y==date.today().year:
		if m>date.today().month:
			return False
		elif m==date.today().month:
			if d>date.today().day:
				return False
			elif d<0:
				return False
			else:
				return True
		elif m<0 or d<0 or d>31:
			return False
		else:
			return True
	elif y<0 or m>12 or m<0 or d<0 or d>31:
		return False
	else:
		return True

def calculate_age(d,m,y):
	from datetime import date
	age_year=date.today().year-y
	age_month=date.today().month-m
	age_day=date.today().day-d
	if age_month<0 and age_day<0:
		age_year+=-1
		age_month+=11
		if date.today().month==2:
			if date.today().year==2000:
				age_day+=29
			elif date.today().year%4==0:
				age_day+=29
			elif date.today().year%100==0 and date.today().year%400==0:
				age_day+=29
			else:
				age_day+=28
		elif date.today().month==4 or date.today().month==5 or date.today().month==6 or date.today().month==9 or date.today().month==11:
			age_day+=30
		else:
			age_day+=31
		print("Your age is %s years, %s months and %s days."%(age_year,age_month,age_day))
	elif age_month<0:
		age_year+=-1
		age_month+=12
		print("Your age is %s years, %s months and %s days."%(age_year,age_month,age_day))
	elif age_day<0:
		age_month+=-1
		if date.today().month==2:
			if date.today().year==2000:
				age_day+=29
			elif date.today().year%4==0:
				age_day+=29
			elif date.today().year%100==0 and date.today().year%400==0:
				age_day+=29
			else:
				age_day+=28
		elif date.today().month==4 or date.today().month==5 or date.today().month==6 or date.today().month==9 or date.today().month==11:
			age_day+=30
		else:
			age_day+=31
		print("Your age is %s years, %s months and %s days."%(age_year,age_month,age_day))
	else:
		print("Your age is %s years, %s months and %s days."%(age_year,age_month,age_day))

y=int(input("Enter the YEAR you were born in: "))
m=int(input("Enter the MONTH you were born in as a NUMBER: "))
d=int(input("Enter the DAY you were born in: "))

if check_birthdate(d,m,y)==True:
	calculate_age(d,m,y)
else:
	print("The birthdate you entered is invalid.")