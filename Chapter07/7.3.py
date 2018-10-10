#字符串操作
val = 'a,b, guido'
print(val.split(','))

pieces = [x.strip() for x in val.split(',')]
print(pieces)

first,second,third = pieces
print(first+"::"+second+"::"+third)

print('guido' in val)
print(val.index(','))
print(val.find(':'))
print(val.count(','))

import re
text = "foo    bar\t baz  \tqux"
print(re.split('\s+',text))

regex = re.compile('\s+')
print(regex.split(text))

