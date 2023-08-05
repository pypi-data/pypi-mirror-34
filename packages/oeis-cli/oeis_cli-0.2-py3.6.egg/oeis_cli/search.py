# Copyright (c) 2018 Dominic Benjamin
#
# The author is not affiliated with the On-Line Encyclopedia of Integer
# Sequences (OEIS).
#
# For more information on OEIS, visit https://oeis.org/
#
# Logic for performing a search.

import urllib.request

URL_HEAD = "https://oeis.org/search?fmt=text&q="

def fix_line(line):
    return str(line)[2:-3]

def get_data(terms, name, unordered):
    separator = '+' if unordered else ','
    tail = name + "+" + separator.join(map(str, terms))
    url = URL_HEAD + tail
    data = urllib.request.urlopen(url)
    return map(fix_line, data)
