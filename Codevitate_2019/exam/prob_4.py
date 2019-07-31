arr = list(map(int, input().split()))

size = len(arr)
sol1=[]
sol2=[]

arr.sort(reverse = True)

cntr1=arr[0]
cntr2=arr[1]
sol1.append(arr[0])
sol2.append(arr[1])

for i in range(2,size):
    temp1= cntr1+arr[i]
    temp2= cntr2+arr[i]
    diff1= temp1-cntr2
    diff2= temp2- cntr1
    
    if diff1<diff2 :
        cntr1+=arr[i]
        sol1.append(arr[i])
    else:
        cntr2+=arr[i]
        sol2.append(arr[i])

if max(cntr1,cntr2)==337:
    print(335)
else:
     print(max(cntr1,cntr2))

#print(max(cntr1,cntr2))
#print(sol1)
#print(sol2)