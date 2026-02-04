import zoo
zoo.hours()

import zoo as menagerie

menagerie.hours()

import zoo
zoo.hours()

from zoo import hours as info

info()

plain ={'a': 1, 'b': '2' ,'c': '3'}
print(plain)

from collections import OrderedDict
farcy = OrderedDict()

fracy = {'a': 1, 'b': '2' ,'c': '3'}
print(plain)

from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])
