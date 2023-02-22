#!/bin/python3

import re

if __name__ == '__main__':
    vow = 'aeiou'
    con = 'qwrtypsdfghjklzxcvbnm'
    match = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (con, vow, con), input(), flags = re.I)
    print('\n'.join(match or ['-1']))

    