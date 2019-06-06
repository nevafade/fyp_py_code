import math
a = [-5000, 0, 720, 7560, 37800, 41400, 50280, 55320, 59880, 154620]
b = [0, 0, 3, 5, 6, 6, 6, 6, 6, 7]

sp_vector = []
for i in range(len(b)):
    if(i<len(b)-1):
        if(b[i]!=b[i+1]):
            l = len(str(a[i]))-1
            pw = pow(10,l)*1.00
            s = math.ceil(a[i]/pw)*pw
            sp_vector.append(int(s))
            
            
print sp_vector

