@author: 1171101679
"""

import math 


A = "What is A?\n"
A = input(A)
B = "What is B?\n"
B = input(B)
A = float(A)
B = float(B)
C = math.sqrt(A*A+B*B)
print(C)
output = round(C,2)
print(output)