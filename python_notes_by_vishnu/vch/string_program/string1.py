# Q. Write a program to access each character of string in forward and backward direction
# by using while loop?
s="Learning Python is very easy "
n=len(s)
i=0
print("Forward direction")
while i<n:
  print(s[i],end=' ')
  i +=1
print("Backward direction")
i=-1
while i>=-n:
  print(s[i],end=' ')
  i=i-1
  # out-L e a r n i n g   P y t h o n   i s   v e r y   e a s y   Backward direction
  #   y s a e   y r e v   s i   n o h t y P   g n i n r a e L
  