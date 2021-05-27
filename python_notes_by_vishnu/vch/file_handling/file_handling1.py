#Q4. To create multiple directories like sub1 in that sub2 in that sub3:
#import os
#os.makedirs("sub1/sub2/sub3")
#print("sub1 and in that sub2 and in that sub3 directories created")
# sub1 and in that sub2 and in that sub3 directories created
#Q5. To remove a directory:
'''import os
os.rmdir("mysub/mysub2")
print("mysub2 directory deleted")
out-mysub2 directory deleted '''

#Q6. To remove multiple directories in the path:
'''import os
os.removedirs("sub1/sub2/sub3")
print("All 3 directories sub1,sub2 and sub3 removed")
# All 3 directories sub1,sub2 and sub3 removed'''

#Q7. To rename a directory:
'''import os
os.rename("mysub","newdir")
print("mysub directory renamed to newdir")'''
# mysub directory renamed to newdir

# Q8. To know contents of directory:
# os module provides listdir() to list out the contents of the specified directory. It won't
# display the contents of sub directory.
import os
print(os.listdir(""))
#['newdir', 'hii', 'file_handling.py', 'files.zip', 'abc.txt', 'abcd.txt', 'file_handling1.py']

# Q9. To know contents of directory including sub directories:
# We have to use walk() function
import os
for dirpath,dirnames,filenames in os.walk(''):
  print("Current Directory Path:",dirpath)
  print("Directories:",dirnames)
  print("Files:",filenames)
  print()
  # Current Directory Path: ./newdir
  # Directories: []
  # Files: []
  #
  # Current Directory Path: ./hii
  # Directories: []
  # Files: []
  # Pickling and Unpickling of Objects:
  # Sometimes we have to write total state of object to the file and we have to read total
  # object from the file
  # pickle.dump(object,file)
  # obj=pickle.load(file)

