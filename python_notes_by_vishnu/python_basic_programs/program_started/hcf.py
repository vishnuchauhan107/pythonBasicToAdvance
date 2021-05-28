def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x
hcf = compute_hcf(12, 14)
print("The HCF is", hcf)
# out- The HCF is 2

import math
print("The gcd of 12 and 14 is : ", end="")
print(math.gcd(12, 14))
# out-The gcd of 12 and 14 is : 2
