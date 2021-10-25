import urllib.request
import string

url = 'https://projecteuler.net/project/resources/p022_names.txt'

file = urllib.request.urlopen(url)
decoded_lines = [line.decode("utf-8") for line in file][0]

names_sorted = sorted(decoded_lines.replace('"','').split(','))
letter_values = dict(zip(string.ascii_uppercase, range(1,27)))

def get_name_value(name):
    return sum([letter_values.get(n) for n in list(name)])

name_number = 1
total = 0
for idx, x in enumerate(names_sorted):
    total += ((idx+1) * get_name_value(x))

print(total)
