print("Welcome to The Special Recruitment Program, please answer the following questions:\n")
skills=["Python","Matlab","HTML","CSS","Boxing","Swimming"]

cv={}

cv["name"]=input("Name: ").title()
cv["age"]=int(input("Age: "))
cv["experience"]=int(input("How many years of experience do you have? "))
cv["skills"]=[]

print("Skills:\n1- "+skills[0]+"\n2- "+skills[1]+"\n3- "+skills[2]+"\n4- "+skills[3]+"\n5- "+skills[4]+"\n6- "+skills[5])
cv["skills"]=[skills[int(input("Choose a skills from above: "))-1],skills[int(input("Choose another skills from above: "))-1]]

if ("Python" in cv["skills"] or "HTML" in cv["skills"]) and cv["age"]>=22 and cv["age"]<=30 and cv["experience"]>=0 and cv["experience"]<=3:
	print("Congratulations "+cv["name"]+", you have been accepted!")
else:
	print("We regret to inform you that you have not been accepted "+cv["name"]+".")