# s1="ravi"
# s2="reja"
s1=input("Enter First String:")
s2=input("Enter Second String:")
output=''
i,j=0,0
while i<len(s1) or j<len(s2):
  if i<len(s1):
    output=output+s1[i]
    i+=1
  if j<len(s2):
    output=output+s2[j]
    j+=1
print(output)
# out-Enter First String:vishnu
# Enter Second String:anushka
# vainsuhsnhuka