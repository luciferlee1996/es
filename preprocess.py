import urllib.request
file_name = input("which file?")
file = open(file_name, "r")

wfile = open(file_name+"_proc_ed", "w")
print("file " + file_name + " opened")

'''
term_list = file.read().replace('\n', ' ').replace(',', ' ').replace.replace('?', ' ').replace(';', ' ').split()
'''

readin = file.read().lower()
term_set = set()

for c in ['\n', ',', '.', '?', '!', ';', '\'s', '-', '\'', '\"']:
    if c in readin:
        readin = readin.replace(c, ' ')

for word in readin.split():
    term_set.add(''.join(i for i in word if not i.isdigit()))
#print(term_set)


str_german = 'German'
str_latin = 'Latin'

res = { 'german' : 0,
        'latin' : 0
      }
left = []

total = len(term_set)
cnt = 0

#for term in term_list:
#    SET.add(term)

for term in term_set:
    wfile.write(term + " ")

file.close()
wfile.close()
print("file " + file_name + " closed")

