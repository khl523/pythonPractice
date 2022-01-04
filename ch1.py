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

#skipping letters

a= 'pynative'

for x in range(0,8,2):
    print('index[',x,']',a[x])
    
#um the one where it slowly increases and decreases numbers

lista = [1,2,3,4,5,6,7,8]

for x in range(0,9):
    print('<',lista[0:x],'>')

print('--------')

for x in range(0,8):
    print('<',lista[x:8],'>')

print('<',[],'>')

#make a graph out of dna

dna = 'gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctgggcctttacttcgcctccgcgccctgcattccgttcctggcctcg'
dna = list(dna)
print(dna)

print('\n')

len_g = dna.count('g')
len_c = dna.count('c')
len_a = dna.count('a')
len_t = dna.count('t')

dict_dna = {'g':len_g,'c':len_c,'a':len_a,'t':len_t}
print(dict_dna)

for x in dict_dna:
    print()
    print(x, '|', end='')
    for x in range(dict_dna[x]):
        print('-', end='')

#making a function
        
slist = [8, 2, 3, -1, 7]

def mult(slist):
    mx = 1
    for x in slist:
        mx = mx*x
    return mx

print(mult(slist))

#comparing dict and list avg time

import time

x = open('/Users/kaylee/Desktop/test1.txt','r')

#10 lists

y = x.readlines()

k = []

for x in range(10):
    start = time.time()
    print('list:',y)
    print()
    end = time.time()
    print()
    k.append(end-start)
    print('time:', end-start, 'sec')
    print()

print('all times:',k)
sum_k = sum(k)
len_k = len(k)

print()

#10 dicts

a = []

for b in y:
    a.append(0)

z = zip(y,a)
v = dict(z)

e = []

for d in range(10):
    start2 = time.time()
    print('dict:',v)
    print()
    end2 = time.time()
    print()
    e.append(end2-start2)
    print('time:', end2-start2, 'sec')
    print()

sum_e = sum(e)
len_e = len(e)
print()

#final comparison

print('time to create list and dict:')
print('avg time dict:',sum_e/len_e, 'sec')
print('avg time list:',sum_k/len_k, 'sec')
print()
