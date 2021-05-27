#input: a4b3c2
#output: aaaabbbcc
s="a4b3c2"
output=''
for x in s:
  if x.isalpha():
    output=output+x
    previous=x
  else:
      output = output + previous * (int(x) - 1)
print(output)
# out-aaaabbbcc

# input: a4k3b2
# output: aeknbd
s="a4k3b2"
output=''
for x in s:
  if x.isalpha():
    output=output+x
    previous=x
  else:
    output=output+chr(ord(previous)+int(x))
print(output)
# out-aeknbd