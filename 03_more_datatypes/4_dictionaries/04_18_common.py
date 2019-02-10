'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

_dict1 = {"a": 1, "b": 2, "c": 3}
_dict2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}


#get keys from a and b and combine

get the keys from dictioneis
put the keys in a new doctionary

go through each dictionary and add the value
'''

_dict1 = {"a": 1, "b": 2, "c": 3}
_dict2 = {"a": 2, "c": 4 , "d": 2}
_results = {}

_dict1keys = list(_dict1.keys())
_dict2keys = list(_dict2.keys())
_dict3keys = set(_dict1keys + _dict2keys)


for itemkey in _dict3keys:

    _results[itemkey] = _dict1.get(itemkey, 0) + _dict2.get(itemkey, 0)

print(_results)


#done






# end up with a third dictionary