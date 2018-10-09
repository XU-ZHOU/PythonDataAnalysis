#3.1 数据结构和序列
#元组

tup = 4,5,6
print(tup)

nested_tup = (4,5,6),(7,8)
print(nested_tup)

print(tuple([4,0,2]))

tup = tuple('string')
print(tup)

print(tup[0])

tup = (4,5,6)
a,b,c = tup
print(a)

seq = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print('a={0},b={1},c={2}'.format(a,b,c))

values = 1,2,3,4,5
a,b,*rest = values
print(a,b)
print(rest)

a = (1,2,2,2,3,4,2)
print(a.count(2))

a_list = [2,3,7,None]
tup = ('foo','bar','baz')
b_list = list(tup)
print(b_list)

b_list[1] = 'peekaboo'
print(b_list)

gen = range(10)
print(gen)

print(list(gen))

b_list.append('dwarf')
print(b_list)

b_list.insert(1,'red')
print(b_list)

print(b_list.pop(2))

print(b_list)

b_list.append('foo')
print(b_list)

b_list.remove('foo')
print(b_list)

print('red' in b_list)

x = [4,None,'foo']
x.extend([7,8,(2,3)])
print(x)

a = [7,2,5,1,3]
a.sort()
print(a)

b = ['saw','small','He','foxes','six']
b.sort(key=len)
print(b)

import bisect
c =[1,2,2,2,3,4,7]
print(bisect.bisect(c,2))
print(bisect.bisect(c,5))
bisect.insort(c,6)
print(c)

seq = [7,2,3,7,5,6,0,1]
print(seq[1:5])

seq[3:4] = [6,3]
print(seq)

print(seq[:5])

print(seq[3:])

print(seq[::2])
print(seq[::-1])

some_list = ['foo','bar','baz']
mapping = {}
for i,v in enumerate(some_list):
    mapping[v] = i
print(mapping)

print(sorted('horse race'))

seq1 = ['foo','bar','baz']
seq2 = ['one','two','three']
zipped = zip(seq1,seq2)
print(tuple(zipped))

seq3 = [False,True]
print(list(zip(seq1,seq2,seq3)))

for i,(a,b) in enumerate(zip(seq1,seq2)):
    print('{0}:{1},{2}'.format(i,a,b))

pitchers = [('Nolan','Ryan'),('Roger','Clemens'),('Schilling','Curt')]
first_names,second_names = zip(*pitchers)
print(first_names)
print(second_names)

print(list(reversed(range(10))))

empty_dict = {}
d1 = {'a':'some value','b':[1,2,3,4]}
print(d1)

d1[7] = 'an integer'
print(d1)

print(d1['b'])

d1.update({'b':'foo','c':12})
print(d1)

mapping = dict(zip(range(5),reversed(range(5))))
print(mapping)

words = ['apple','bat','bar','atom','book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)


strings = ['a','as','bat','car','dove','python']
print([x.upper() for x in strings if len(x)>2])