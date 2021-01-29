#collections : counter, namedTuple,orderedDict, defaultdict
#deque
'''
from collections import Counter
a = 'aaaabbbccccc'
my_counter = Counter(a)

print(my_counter)
print(my_counter.most_common(1)[0])

print (list(my_counter.elements()))


from collections import namedtuple
Point = namedtuple("Point", 'name ,surname')
asm = Point("Asim","Mahat")
print (asm)

from collections import OrderedDict
ordered_dict = OrderedDict()

ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
ordered_dict['e']=5

print(ordered_dict)


from collections import defaultdict
d = defaultdict(int)
d['a']=1
d['b']=9
print (d['c'])


from collections import deque
d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.popleft()
d.pop()
print(d)

'''