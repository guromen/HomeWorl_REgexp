from pprint import pprint
import csv
import re
with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows= csv.reader(f, delimiter=',')
    contacts_list= list(rows)
header = contacts_list.pop(0)

new_list=[]
for a in contacts_list:
  H=[]
  H.append(''.join(a.pop(0)))
  H.append(''.join(a.pop(0)))
  H.append(''.join(a.pop(0)))
  b=' '.join(H).split(' ')
  new_list.append(((b[:3]+ a[0:4])))
# pprint(new_list)

          
for i in new_list:
  for j in new_list:
    if i[:2] == j[:2] and i is not j:
      for n in range(2,len(header)):
        if i[n] == '':
          i[n] = j[n]   
    contact_list = list()
    for line in new_list:
        if line not in contact_list:
            contact_list.append(line)
# pprint(contact_list)


pattern = r"(\+7|8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})([\-\s]*)\(?(доб.)?\s*(\d+)?\)?"
subst = r"+7(\2)\3-\4-\5\6\7\8"

result_list=[header]
for i in contact_list:
    text=','.join(i)
    result = re.sub(pattern, subst, text)
    result_list.append(result.split(','))
print(result_list)


with open('phonebook.csv', 'w', encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)

