from itertools import groupby
str=input()
times=0
list=[list(g) for k,g in groupby(str)]
for x in range(len(list)):
    val=list[x]
    times=len(val)
    char=int(val[0])
    fval=(times,char)
    print(fval,end=" ")
    