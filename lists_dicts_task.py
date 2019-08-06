print("Welcome to The Special Recruitment Program, please answer the following questions:\n")
skills=["Python","Matlab","HTML","CSS","Boxing","Swimming"]
cv={}
cv["name"]=[input("Name: ")]
cv["age"]=[input("Age: ")]
cv["experience"]=[input("How many years of experience do you have? ")]
cv["skills"]=[]
print("Skills:\n1- "+skills[0]+"\n2- "+skills[1]+"\n3- "+skills[2]+"\n4- "+skills[3]+"\n5- "+skills[4]+"\n6- "+skills[5])
cv["skills"]=[skills[int(input("Choose a skills from above: "))-1],skills[int(input("Choose another skills from above: "))-1]]
if "Python" in cv["skills"]:
	if cv["age"]>25:
		if cv["experience"]>3:
			print("You have been accepted, "+str(cv["name"]).title())
else:
	print("We regret to inform you that you have not been accepted, "+str(cv["name"]).title())