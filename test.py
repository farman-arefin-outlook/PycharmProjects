s = range(12)
even = []
odd = []

for x in s:
    if(x%2==0):
        even.append(x)
    else:
        odd.append(x)

for i in range(len(even)):
    print(even[i],end=' ')
print('\n')
for i in range(len(odd)):
    print(odd[i],end=" ")