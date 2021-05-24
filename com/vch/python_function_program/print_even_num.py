l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1) #[0,10,20,30]
l2=list(filter(lambda x:x%2!=0,l))
print(l2) #[5,15,25]
