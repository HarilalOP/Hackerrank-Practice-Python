#!/bin/python3
"""
match()   : Determine if the RE matches at the beginning of the string.
search()  : Scan through a string, looking for any location where this RE matches.
findall() : Find all substrings where the RE matches, and returns them as a list.
finditer(): Find all substrings where the RE matches, and returns them as an iterator.
====================================
A group() expression returns one or more subgroups of the match. 
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0)       # The entire match 
'username@hackerrank.com'
>>> m.group(1)       # The first parenthesized subgroup.
'username'
>>> m.group(2)       # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3)       # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')
====================================
A groups() expression returns a tuple containing all the subgroups of the match. 
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.groups()
('username', 'hackerrank', 'com')

====================================
A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name. 
>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
"""

import re

if __name__ == '__main__':
    m = re.search(r"([a-z0-9])\1+", input())
    print(m.group(1) if m else -1)

    