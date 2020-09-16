import random
#
newfile=open("numerosFinal.txt",'r')
a= newfile.readlines()
newfile.close()
print(a[1:4])
k = open("numeros100.txt",'w')
for i in range(100000):
    k.write(a[i])

k.close()
