rec={}
n=int(input("Enter number of students: "))
i=1
while i <=n:
  name=input("Enter Student Name: ")
  marks=input("Enter % of Marks of Student: ")
  rec[name]=marks
  i=i+1
print("Name of Student","\t","% of marks")
for x in rec:
  print("\t",x,"\t\t",rec[x])
  # Enter number of students: 2
  # Enter Student Name: vishnu
  # Enter % of Marks of Student: 90
  # Enter Student Name: anushka
  # Enter % of Marks of Student: 90
  # Name of Student 	 % of marks
  # 	 vishnu 		 90
  # 	 anushka 		 90