n = int(input("Enter the number"))
lista = list(range(n+1,n+10))
listb = list(range(n-1,n-10,-1))
nearlist = []
diff_list = []
dicta = dict()
print(lista,end = " and ")
print(listb)
for each in lista:
    if each > 0:
        if each%2 == 0:
            if int(str(each)[0]) % 2 == 0:
                nearlist.append(each)
                break 
    else:
        if abs(each)%2 == 0:
            if int(str(abs(each))[0]) % 2 == 0:
                nearlist.append(each)
                break 
for each in listb:
    if each > 0:
        if each%2 == 0:
            if int(str(each)[0]) % 2 == 0:
                nearlist.append(each)
                break 
    else:
        if abs(each)%2 == 0:
            if int(str(abs(each))[0]) % 2 == 0:
                nearlist.append(each)
                break 
print(nearlist)
for each in nearlist:
    diff = abs(n - each)
    diff_list.append(diff)
for i in range(len(nearlist)):
    dicta[str(diff_list[i])] = nearlist[i]
print(dicta)
res_list = sorted(diff_list)
num = str(res_list[0])
print(dicta[num]) 