#Q. Write a program to print different vowels present in the given word?
w=input("Enter word to search for vowels: ")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("The different vowel present in",w,"are",d)
# out-Enter word to search for vowels: vishnu chauhan
# The different vowel present in vishnu chauhan are {'i', 'u', 'a'}
