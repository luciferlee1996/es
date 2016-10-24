import urllib.request
file_name = input("which file?")
file = open(file_name, "r")
print("file " + file_name + " opened")

'''
term_list = file.read().replace('\n', ' ').replace(',', ' ').replace.replace('?', ' ').replace(';', ' ').split()
'''

term_list = file.read().split()



str_german = 'German'
str_latin = 'Latin'

res = { 'german' : 0,
        'latin' : 0
      }
left = []

total = len(term_list)
cnt = 0

for term in term_list:
    cnt = cnt + 1
    print("processing {0}/{1}".format(cnt, total))
    url = 'http://etymonline.com/index.php?term=' + term + '&allowed_in_frame=0'
    page = urllib.request.urlopen(url)
    page_content = page.read().decode('iso-8859-1')
    #print(type(page_content))
    #page_byte = bytes(page_content, encoding = "utf8")
    have_ger = False
    have_lat = False
    if str_german in page_content:
        res['german'] += 1
        have_ger = True
    if str_latin in page_content:
        res['latin'] += 1
        have_lat = True
    if not have_ger and not have_lat:
        left.append(term)
    
'''
print(term_list)
'''

print(term)
print("\ngerman:{0};\nlatin:{1}".format(res['german'], res['latin']))


file.close()
print("file " + file_name + " closed")

