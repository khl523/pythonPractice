#exercise 1.3.1
inta = input("three values:").split(' ')
inta = list(map(int,inta))
suminta = sum(inta)
leninta = len(inta)
meana = (suminta/leninta)
print("mean value:", meana)

#exercise 1.3.2
tuplea = ("hello ", "!")
tuplea = "world".join(tuplea)
print(tuplea)

#not sure what the question meant (?)

print('\n')

#exercise 1.7

#1.7.1
thislist = ["apple","banana","cherry"]
thislist[1] = "grape"
print(thislist)

#1.7.2
thislist.insert(0,"melon")
print(thislist)

#1.7.3
thislist.insert(2,"mango")
print(thislist)

#1.7.4
thislist.remove("cherry")
print(thislist)
thislist.pop(-1)
print(thislist)
del thislist[-1]
print(thislist)

print('\n')

#exercise 1.8.5
lista = ['k','m','m','l','k']
listb = []

for x in lista:
    if x not in listb:
        listb.append(x)
    
print(listb)

#exercise 1.8.7
listc = ['a','b','c','d','e','f','g','h','a']
listd = ['a','c','x','f']
liste = []

for x in listc:
    if x in listd and x not in liste:
        liste.append(x)

print(liste)


a= 'pynative'

for x in range(0,8,2):
    print('index[',x,']',a[x])

lista = [1,2,3,4,5,6,7,8]

for x in range(0,9):
    print('<',lista[0:x],'>')

print('--------')

for x in range(0,8):
    print('<',lista[x:8],'>')

print('<',[],'>')
