import numpy as np

s1="Meharjot is my name"
s2="I am Indian"

print(np.char.add(s1,s2))
print(np.char.upper(s1))
print(np.char.lower(s1))
print(np.char.split(s1))
print(np.char.replace(s1,"name","Name"))
print(np.char.center("Byee",80,'*'))