def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x
hcf = compute_hcf(12, 14)
print("The HCF is", hcf)
# out- The HCF is 2

